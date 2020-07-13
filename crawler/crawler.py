
import pickle
import redis
import random
import asyncio

from yamaps.yamaps import YaMaps
from map_bboxer.map_bboxer import MapBboxer
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty


class Crawler:

    def __init__(self, db, yamap, request_params, bbox, max_workers_count=16):
        self.__db = db
        self.__yamap = yamap
        self.__request_params = request_params
        self.__bbox = bbox
        self.__max_workers_count = max_workers_count
        self.__bbox_queue = asyncio.Queue()
        self.__features_queue = asyncio.Queue()
        self.__new_objects_queue = asyncio.Queue()

    async def run(self):
        print("Start Bboxing")
        map_bboxing = await self.__get_map_bboxing()
        print("bboxing OK", map_bboxing)
        await self.__fill_bbox_queue(map_bboxing)
        print("fill_bbox_queue OK")
        await self.__run_bbox_workers()
        print("run_bbox_workers OK")
        await self.__run_feature_workers()
        print("run_feature_workers OK")

    async def __run_feature_workers(self):
        workers = [self.__feature_worker() for _ in range(self.__max_workers_count)]
        await asyncio.gather(*workers)

    async def __feature_worker(self):
        while not self.__features_queue.empty():
            feature = await self.__features_queue.get()
            try:
                await self.__handle_feature(feature)

            except MissingRequiredProperty as handler:
                handler(str(hex(random.getrandbits(128))))
                await self.__handle_feature(feature)

            except KeyError as e:
                print("something wrongs", e)                #TOOD loggining

            except Exception as e:
                print("Oopse", e)                           #TOOD loggining

    async def __handle_feature(self, feature):
        if not self.__db.exists(feature.company_meta_data.id):
            await self.__new_objects_queue.put(feature)
            self.__db.set(feature.company_meta_data.id, pickle.dumps(feature))

    async def __run_bbox_workers(self):
        workers_futures = [self.__bbox_worker() for _ in range(self.__max_workers_count)]
        await asyncio.gather(*workers_futures)

    async def __bbox_worker(self):
        while not self.__bbox_queue.empty():
            bbox = await self.__bbox_queue.get()
            text_bbox = f"{bbox[0][0]},{bbox[0][1]}~{bbox[1][0]},{bbox[1][1]}"
            yandex_response = await self.__yamap.request(**self.__request_params, bbox=text_bbox)
            await self.__fill_features_queue(yandex_response.features)

    async def __fill_features_queue(self, features):
        put_features_futures = [self.__features_queue.put(feature) for feature in features]
        await asyncio.gather(*put_features_futures)

    async def __fill_bbox_queue(self, map_bboxing):
        if type(map_bboxing) is list:
            for bbox in map_bboxing:
                await self.__bbox_queue.put(bbox)

    async def __get_map_bboxing(self):
        map_bboxing = await self.__load_map_bboxing()
        if not (type(map_bboxing) is list) or not(len(map_bboxing)):
            map_bboxing = await self.__update_map_bboxing()

        return map_bboxing

    async def __load_map_bboxing(self):
        map_bboxing_pickle = self.__db.get("map_bboxing")
        if map_bboxing_pickle:
            self.__db.set("map_bboxing", map_bboxing_pickle)
            return pickle.loads(map_bboxing_pickle)
        return []

    async def __update_map_bboxing(self):
        bboxer = MapBboxer(self.__yamap, self.__request_params, self.__bbox)
        await bboxer.start_bboxing()
        map_bboxing = await bboxer.get_out_list()

        await self.__set_map_bboxing(map_bboxing)
        return map_bboxing

    async def __set_map_bboxing(self, map_bboxing):
        if type(map_bboxing) is list:
            pickle_map_bboxing = pickle.dumps(map_bboxing)
            self.__db.set("map_bboxing", pickle_map_bboxing)

    async def get_new_objects_queue(self): #TODO normal getter
        return self.__new_objects_queue

    async def get_new_objects_list(self):

        futures = [self.__new_objects_queue.get() for _ in range(self.__new_objects_queue.qsize())]
        return await asyncio.gather(*futures)



