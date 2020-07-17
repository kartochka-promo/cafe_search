
import unittest
import asyncio
from typing import Any

from map_bboxer.map_bboxer import MapBboxer
from yamaps.yamaps import YaMaps


def async_test(f):
    """
    Декаратор, преобразующий async функцию в обычную для u

    :type f: function
    :param f: функция для обёртки
    :rtype: function
    :return: возвращает декорированную функцию
    """
    def wrapper(*args: Any, **kwargs: Any):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)

    return wrapper


class TestMapBboxer(unittest.TestCase):
    """
    Класс для тестирования класса MapBboxer
    Запуск тестов - coverage3 run --source cafe_search/ -m unittest discover cafe_search
    Покрытие coverage report -m
    """

    @async_test
    async def test_init(self):
        """ Тест на конструктор класса MapBboxer """

        y_map: type(YaMaps) = YaMaps("12b9aefasc-0000-49ae-1233-65ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-0000-49ae-1233-65ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            map_bboxer = MapBboxer(y_map, {}, [[0, 0], [1, 1]])

    @async_test
    async def test_get_out_queue(self):
        """ Тест на получение очереди результатов разбиения """

        y_map: type(YaMaps) = YaMaps("12b9aefasc-0000-49ae-1233-65ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-0000-49ae-1233-65ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            map_bboxer = MapBboxer(y_map, {}, [[0, 0], [1, 1]])
            self.assertIs(type(await map_bboxer.get_out_queue()), asyncio.Queue)

    @async_test
    async def test_get_out_queue(self):
        """ Тест на получение списка результатов разбиения """

        y_map: type(YaMaps) = YaMaps("12b9aefasc-0000-49ae-1233-65ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-0000-49ae-1233-65ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            map_bboxer = MapBboxer(y_map, {}, [[0, 0], [1, 1]])
            self.assertEqual(await map_bboxer.get_out_list(), [])

    @async_test
    async def test_split_bbox_by_x(self):
        """ Тест на разбиение bbox по вертикали на две равные части """

        y_map: type(YaMaps) = YaMaps("12b9aefasc-0000-49ae-1233-65ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-0000-49ae-1233-65ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            map_bboxer = MapBboxer(y_map, {}, [])
            self.assertEqual(await map_bboxer._split_bbox_by_x([[0, 0], [1, 2]]),
                             [[[0, 0], [0.5, 2]], [[0.5, 0], [1, 2]]])

            self.assertEqual(await map_bboxer._split_bbox_by_x([[2, 5], [5, 10]]),
                             [[[2, 5], [3.5, 10]], [[3.5, 5], [5, 10]]])

    @async_test
    async def test_split_bbox_by_y(self):
        """ Тест на разбиение bbox по горизонтали на две равные части """

        y_map: type(YaMaps) = YaMaps("12b9aefasc-0000-49ae-1233-65ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-0000-49ae-1233-65ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            map_bboxer = MapBboxer(y_map, {}, [])
            self.assertEqual(await map_bboxer._split_bbox_by_y([[0, 0], [1, 2]]),
                             [[[0, 0], [1, 1]], [[0, 1], [1, 2]]])

            self.assertEqual(await map_bboxer._split_bbox_by_y([[2, 5], [5, 10]]),
                             [[[2, 5], [5, 7.5]], [[2, 7.5], [5, 10]]])

    @async_test
    async def test_split_bbox(self):
        """ Тест на разбиение bbox по большей стороне на две равные части """

        y_map: type(YaMaps) = YaMaps("12b9aefasc-0000-49ae-1233-65ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-0000-49ae-1233-65ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            map_bboxer = MapBboxer(y_map, {}, [])
            self.assertEqual(await map_bboxer._split_bbox([[0, 0], [1, 2]]),
                             [[[0, 0], [1, 1]], [[0, 1], [1, 2]]])

            self.assertEqual(await map_bboxer._split_bbox([[2, 5], [5, 6]]),
                             [[[2, 5], [3.5, 6]], [[3.5, 5], [5, 6]]])


if __name__ == '__main__':
    unittest.main()
