
import pickle
import random
import asyncio
from typing import List
from typing import Dict

from yamaps.yamaps import YaMaps
from map_bboxer.map_bboxer import MapBboxer
from yamaps.yandex_response.feature.feature import Feature
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty


class Crawler:
    """ Класс, который производит поиск новых объектов в секторе (bbox). """

    def __init__(self, db, yamap: YaMaps, request_params: Dict, bbox: List[List[float]], max_workers_count: int = 16):
        """
        Конструктор класса Crawler

        :param db: база данных для хранения существующих объектов

        :type yamap: YaMaps
        :param yamap: объект для отправки запросов к YandexApi

        :type request_params: Dict
        :param request_params: словарь параметров запроса, передающихся в YaMaps

        :type bbox: List[List[float]]
        :param bbox: Список из двух точек (левый нижний угол поиска и правый верхний),
            которые описывают область поиска (bbox)

        :type max_workers_count: int
        :param max_workers_count: максимальное колличество ассинхронных процессов, которые проводят поиск новых объектов

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__db = db
        self.__yamap: YaMaps = yamap
        self.__request_params: Dict = request_params
        self.__bbox: List[List[float]] = bbox
        self.__max_workers_count: int = max_workers_count
        self.__bbox_queue: asyncio.Queue = asyncio.Queue()
        self.__features_queue: asyncio.Queue = asyncio.Queue()
        self.__new_objects_queue: asyncio.Queue = asyncio.Queue()

    async def run(self):
        """
        Метод, который запускает процесс поиска новых объектов

        :rtype: None
        :return: Ничего не возвращает
        """

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
        """
        Метод, который запускает воркеров, которые обрабатывают ответ от YaMaps

        :rtype: None
        :return: Ничего не возвращает
        """

        workers = [self.__feature_worker() for _ in range(self.__max_workers_count)]
        await asyncio.gather(*workers)

    async def __feature_worker(self):
        """
        Воркер, который обрабатывает ответы от YaMaps

        :rtype: None
        :return: Ничего не возвращает
        """

        while not self.__features_queue.empty():
            feature = await self.__features_queue.get()
            try:
                await self.__handle_feature(feature)

            except MissingRequiredProperty as handler:
                handler(str(hex(random.getrandbits(128))))
                await self.__handle_feature(feature)

            except KeyError as e:
                print("something wrongs", e)                            # TODO loggining

            except Exception as e:
                print("Oopse", e)                                       # TODO loggining

    async def __handle_feature(self, feature: Feature):
        """
        Метод, который проверяет объект на новизну

        :type feature: Feature
        :param feature: информация о найденном объекте

        :rtype: None
        :return: Ничего не возвращает
        """

        if not self.__db.exists(feature.company_meta_data.id):
            await self.__new_objects_queue.put(feature)
            self.__db.set(feature.company_meta_data.id, pickle.dumps(feature))

    async def __run_bbox_workers(self):
        """
        Метод, который запускает вокеров, которые осуществляют поиск объектов в области

        :rtype: None
        :return: Ничего не возвращает
        """

        workers_futures = [self.__bbox_worker() for _ in range(self.__max_workers_count)]
        await asyncio.gather(*workers_futures)

    async def __bbox_worker(self):
        """
        Воркер который осуществляют поиск объектов в области

        :rtype: None
        :return: Ничего не возвращает
        """

        while not self.__bbox_queue.empty():
            bbox = await self.__bbox_queue.get()
            text_bbox = f"{bbox[0][0]},{bbox[0][1]}~{bbox[1][0]},{bbox[1][1]}"
            yandex_response = await self.__yamap.request(**self.__request_params, bbox=text_bbox)
            await self.__fill_features_queue(yandex_response.features)

    async def __fill_features_queue(self, features):
        """
        Метод, который реализует загрузку объектов, найденных в bbox в очередь.

        :type features: List[Feature]
        :param features: информация о найденных объектах

        :rtype: None
        :return: Ничего не возвращает
        """

        put_features_futures = [self.__features_queue.put(feature) for feature in features]
        await asyncio.gather(*put_features_futures)

    async def __fill_bbox_queue(self, map_bboxing):
        """
        Метод, который реализует загрузку разбиений(bbox) области поиска, в очередь.

        :type map_bboxing: List[List[List[float]]]
        :param map_bboxing: список разбиений области поиска

        :rtype: None
        :return: Ничего не возвращает
        """
        if type(map_bboxing) is list:
            futures = [self.__bbox_queue.put(bbox) for bbox in map_bboxing]
            await asyncio.gather(*futures)

    async def __get_map_bboxing(self):
        """
        Метод, который получает текущее разбиение области поиска

        :rtype: List[List[List[float]]]
        :return: разбиение области поиска
        """
        map_bboxing = await self.__load_map_bboxing()
        if not (type(map_bboxing) is list) or not(len(map_bboxing)):
            map_bboxing = await self.__update_map_bboxing()

        return map_bboxing

    async def __load_map_bboxing(self):
        """
        Метод, который загружает текущее разбиение области поиска

        :rtype: List[List[List[float]]]
        :return: разбиение области поиска
        """

        map_bboxing_pickle = self.__db.get("map_bboxing")
        if map_bboxing_pickle:
            self.__db.set("map_bboxing", map_bboxing_pickle)
            return pickle.loads(map_bboxing_pickle)
        return []

    async def __update_map_bboxing(self):
        """
        Метод, который обновляет текущее разбиение области поиска

        :rtype: List[List[List[float]]]
        :return: разбиение области поиска
        """

        bboxer = MapBboxer(self.__yamap, self.__request_params, self.__bbox)
        await bboxer.start_bboxing()
        map_bboxing = await bboxer.get_out_list()

        await self.__set_map_bboxing(map_bboxing)
        return map_bboxing

    async def __set_map_bboxing(self, map_bboxing):
        """
        Метод, который сохраняет текущее разбиение области поиска

        :type map_bboxing: List[List[List[float]]]
        :param map_bboxing: текущее разбиение области поиска

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(map_bboxing) is list:
            pickle_map_bboxing = pickle.dumps(map_bboxing)
            self.__db.set("map_bboxing", pickle_map_bboxing)

    async def get_new_objects_queue(self):                  # TODO normal getter
        """
        Getter который возвращает очередь с найденными объектами

        :rtype: asyncio.Queue
        :return: очередь с найденными объектами
        """

        return self.__new_objects_queue

    async def get_new_objects_list(self):                    # TODO normal getter
        """
        Getter который возвращает список найденных объектов

        :rtype: List[Feature]
        :return: список найденных объектов
        """

        futures = [self.__new_objects_queue.get() for _ in range(self.__new_objects_queue.qsize())]
        return await asyncio.gather(*futures)
