
import asyncio
from yamaps.yamaps import YaMaps
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty


class MapBboxer:

    def __init__(self, yamap, request_params, bbox, bbox_threshold=500, max_workers_count=32):
        self.__yamap = yamap
        self.__request_params = request_params
        self.__bbox = bbox
        self.__bbox_threshold = bbox_threshold
        self.__max_workers_count = max_workers_count
        self.__queue = asyncio.Queue()
        self._out_queue = asyncio.Queue()
        self.__futures = []

    async def start_bboxing(self):
        await self.__queue.put(self.__bbox)
        await self.__generate_worker()

        done = []
        while len(done) != len(self.__futures):
            done, _ = await asyncio.wait(self.__futures)

    async def __generate_worker(self):
        if len(self.__futures) < self.__max_workers_count:
            self.__futures.append(asyncio.ensure_future(self.__bbox_worker()))

    async def __bbox_worker(self):
        while not self.__queue.empty():
            bbox = await self.__queue.get()
            objects_count = await self.__get_objects_in_bbox(bbox)
            print(objects_count)

            if objects_count > self.__bbox_threshold:
                split_bbox = await self.__split_bbox(bbox)
                await self.__queue.put(split_bbox[0])
                await self.__queue.put(split_bbox[1])
                await self.__generate_worker()

            else:
                await self._out_queue.put(bbox)

    async def __split_bbox(self, bbox):
        x_distance = bbox[1][0] - bbox[0][0]
        y_distance = bbox[1][1] - bbox[0][1]

        if x_distance > y_distance:
            return await self.__split_bbox_by_x(bbox)
        else:
            return await self.__split_bbox_by_y(bbox)

    async def __get_objects_in_bbox(self, bbox):
        text_bbox = f"{bbox[0][0]},{bbox[0][1]}~{bbox[1][0]},{bbox[1][1]}"
        ya_response = await self.__yamap.request(**self.__request_params, bbox=text_bbox)

        try:
            return ya_response.response_meta_data.search_response.found
        except MissingRequiredProperty:
            return 0
        except AttributeError:
            return 0
        except Exception as e:
            print(e)

    async def __split_bbox_by_x(self, bbox):
        x_mean = (bbox[1][0] + bbox[0][0]) / 2
        lower_shard = [[bbox[0][0], bbox[0][1]], [x_mean, bbox[1][1]]]
        higher_shard = [[x_mean, bbox[0][1]], [bbox[1][0], bbox[1][1]]]

        return [lower_shard, higher_shard]

    async def __split_bbox_by_y(self, bbox):
        y_mean = (bbox[1][1] + bbox[0][1]) / 2
        lower_shard = [[bbox[0][0], bbox[0][1]], [bbox[1][0], y_mean]]
        higher_shard = [[bbox[0][0], y_mean], [bbox[1][0], bbox[1][1]]]

        return [lower_shard, higher_shard]


# async def test():
#     async with YaMaps("37b33a30-d0da-4053-aee9-07230f897a46") as yamap:
#         request_params = {
#             "text": "Кофейни",
#             "lang": "ru_RU",
#             "type": "biz",
#             "rspn": "1",
#             "results": "500"
#         }
#         bbox = [[37.048427, 55.43644866], [38.175903, 56.04690174]]
#
#         bboxer = MapBboxer(yamap, request_params, bbox)
#         await bboxer.start_bboxing()
#         while not bboxer._out_queue.empty():
#             print(await bboxer._out_queue.get())
#
# loop = asyncio.get_event_loop()
# result = loop.run_until_complete(test())
