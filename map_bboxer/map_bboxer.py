
import asyncio
from typing import Dict
from typing import List

from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty
from yamaps.yamaps import YaMaps
from yamaps.yandex_response.yandex_response import YandexResponse


class MapBboxer:
    """
    Класс, который производит разбиение прямоугольного сектора (bbox)
    на составлющие части так, чтобы в каждом секторе было < bbox_threshold объектов.
    """

    def __init__(self, yamap: YaMaps, request_params: Dict, bbox: List[List[float]],
                 bbox_threshold: int = 500, max_workers_count: int = 32) -> None:
        """
        Конструктор класса MapBboxer

        :type yamap: YaMaps
        :param yamap: объект для отправки запросов к YandexApi

        :type request_params: Dict
        :param request_params: словарь параметров запроса, передающихся в YaMaps

        :type bbox: List[List[float]]
        :param bbox: Список из двух точек (левый нижний угол поиска и правый верхний), которые описывают bbox

        :type bbox_threshold: int
        :param bbox_threshold: максимальное колличество объектов в каждом участке разбиения

        :type max_workers_count: int
        :param max_workers_count: максимальное колличество ассинхронных процессов, которые проводят разбиение

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__yamap: YaMaps = yamap
        self.__request_params: Dict = request_params
        self.__bbox: List[List[float]] = bbox
        self.__bbox_threshold: int = bbox_threshold
        self.__max_workers_count: int = max_workers_count
        self.__queue: asyncio.Queue = asyncio.Queue()
        self.__out_queue: asyncio.Queue = asyncio.Queue()
        self.__futures = []

    async def start_bboxing(self) -> None:
        """
        Метод, который запускает процесс разбиения

        :rtype: None
        :return: Ничего не возвращает
        """

        await self.__queue.put(self.__bbox)
        await self._generate_worker()

        done: List = []
        while len(done) != len(self.__futures):             # TODO наверное можно лучше
            done, _ = await asyncio.wait(self.__futures)

    async def _generate_worker(self) -> None:
        """
        Метод, который инициализирует одного ассинхронного воркера

        :rtype: None
        :return: Ничего не возвращает
        """

        if len(self.__futures) < self.__max_workers_count:
            self.__futures.append(asyncio.ensure_future(self._bbox_worker()))

    async def _bbox_worker(self) -> None:
        """
        Воркер, который производит разбиение

        :rtype: None
        :return: Ничего не возвращает
        """

        while not self.__queue.empty():
            bbox: List[List[float]] = await self.__queue.get()
            objects_count: int = await self._get_objects_in_bbox(bbox)

            if objects_count > self.__bbox_threshold:
                split_bbox: List[List[List[float]]] = await self._split_bbox(bbox)
                await self.__queue.put(split_bbox[0])
                await self.__queue.put(split_bbox[1])
                await self._generate_worker()

            else:
                await self.__out_queue.put(bbox)

    async def _split_bbox(self, bbox: List[List[float]]) -> List[List[List[float]]]:
        """
        Метод, делящий bbox пополам поперёк большей стороны

        :type bbox: List[List[float]]
        :param bbox: Список из двух точек (левый нижний угол поиска и правый верхний), для разбиения

        :rtype: List[List[List[float]]]
        :return: Возращает два bbox
        """

        x_distance: float = bbox[1][0] - bbox[0][0]
        y_distance: float = bbox[1][1] - bbox[0][1]

        if x_distance > y_distance:
            return await self._split_bbox_by_x(bbox)
        else:
            return await self._split_bbox_by_y(bbox)

    async def _get_objects_in_bbox(self, bbox: List[List[float]]) -> int:
        """
        Метод который возвращает число найденных объектов в области(bbox)

        :type bbox: List[List[float]]
        :param bbox: bbox(список из двух точек) в котором происходит поиск объектов

        :rtype: int
        :return: число объектов в области
        """

        text_bbox: str = f"{bbox[0][0]},{bbox[0][1]}~{bbox[1][0]},{bbox[1][1]}"
        ya_response: YandexResponse = await self.__yamap.request(**self.__request_params, bbox=text_bbox)

        try:
            return ya_response.response_meta_data.search_response.found
        except MissingRequiredProperty:
            return 0
        except AttributeError:
            return 0
        except Exception as e:
            print(e)

    async def _split_bbox_by_x(self, bbox: List[List[float]]) -> List[List[List[float]]]:
        """
        Метод, производящий разделение bbox(списка из двух точек)
        по оси x на две равные части

        :type bbox: List[List[float]]
        :param bbox: bbox(список из двух точек)

        :rtype: List[List[List[float]]]
        :return: Возвращает две полученные области
        """

        x_mean: float = (bbox[1][0] + bbox[0][0]) / 2
        lower_shard: List[List[float]] = [[bbox[0][0], bbox[0][1]], [x_mean, bbox[1][1]]]
        higher_shard: List[List[float]] = [[x_mean, bbox[0][1]], [bbox[1][0], bbox[1][1]]]

        return [lower_shard, higher_shard]

    async def _split_bbox_by_y(self, bbox: List[List[float]]) -> List[List[List[float]]]:
        """
        Метод, производящий разделение bbox(списка из двух точек)
        по оси y на две равные части

        :type bbox: List[List[float]]
        :param bbox: bbox(список из двух точек)

        :rtype: List[List[List[float]]]
        :return: Возвращает две полученные области
        """

        y_mean: float = (bbox[1][1] + bbox[0][1]) / 2
        lower_shard: List[List[float]] = [[bbox[0][0], bbox[0][1]], [bbox[1][0], y_mean]]
        higher_shard: List[List[float]] = [[bbox[0][0], y_mean], [bbox[1][0], bbox[1][1]]]

        return [lower_shard, higher_shard]

    async def get_out_queue(self) -> asyncio.Queue:  # TODO pretty getters
        """
        Getter возвращающий очередь, с полученными областями разбиения

        :rtype: asyncio.Queue
        :return: очередь, с полученными областями разбиения
        """

        return self.__out_queue

    async def get_out_list(self) -> List:   # TODO pretty getters
        """
        Getter возвращающий список, с полученными областями разбиения

        :rtype: asyncio.Queue
        :return: очередь, с полученными областями разбиения
        """

        futures = [self.__out_queue.get() for _ in range(self.__out_queue.qsize())]
        return await asyncio.gather(*futures)
