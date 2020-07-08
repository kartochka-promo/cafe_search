
import unittest
import asyncio
from typing import Any
from ..yamaps import YaMaps


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


class TestYaMaps(unittest.TestCase):
    """
    Класс для тестирования класса YaMaps
    Запуск тестов - coverage3 run --source yamaps/ -m unittest discover yamaps -v
    Покрытие coverage report -m
    """

    def test_init(self):
        """ Тест на конструктор класса YaMaps """
        y_map: type(YaMaps) = YaMaps("12b9aefasc-0000-49ae-bfe2-65ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-0000-49ae-bfe2-65ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)

        y_map: type(YaMaps) = YaMaps("12b9ac-0d5e-49ae-0000-ab5ed6cb6asa16")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9ac-0d5e-49ae-0000-ab5ed6cb6asa16"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)

        y_map: type(YaMaps) = YaMaps("12b9aefc-099e-49ae-bfe2-75e788c61812")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefc-099e-49ae-bfe2-75e788c61812"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)

        y_map: type(YaMaps) = YaMaps("1888aefc-0d5e-478e-bfe2-75e456761816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=1888aefc-0d5e-478e-bfe2-75e456761816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)

    @async_test
    async def test_open(self):
        """ Тест на открытие и закрытие сессии, функции _open и _close """

        y_map: type(YaMaps) = YaMaps("12b9aefasc-00005ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-00005ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        y_map._open()
        await y_map._close()

        y_map: type(YaMaps) = YaMaps("12b9ac-0-ab5ed6cb6asa16")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9ac-0-ab5ed6cb6asa16"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        y_map._open()
        await y_map._close()

        y_map: type(YaMaps) = YaMaps("12b9aef8c61812")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aef8c61812"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        y_map._open()
        await y_map._close()

        y_map: type(YaMaps) = YaMaps("1478e-bfe2-75e456761816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=1478e-bfe2-75e456761816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        y_map._open()
        await y_map._close()

    def test_generate_request(self):
        """ Тест на генерирование Get запроса, функция generate_request """

        y_map: type(YaMaps) = YaMaps("12b9aefasc-1111-49ae-bfe2-65ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-1111-49ae-bfe2-65ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        request = y_map._generate_request(text="rr", lang="ru_RU")
        self.assertEqual(url + "&text=rr&lang=ru_RU", request)

        y_map: type(YaMaps) = YaMaps("12b9ac-e-0000-ab5ed6cb6asa16")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9ac-e-0000-ab5ed6cb6asa16"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        request = y_map._generate_request(text="Кофе", lang="en_EN")
        self.assertEqual(url + "&text=Кофе&lang=en_EN", request)

        y_map: type(YaMaps) = YaMaps("12b9aefc-099e-49ae-basld5e788c61812")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefc-099e-49ae-basld5e788c61812"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        request = y_map._generate_request(text="Coffe", lang="ru_RU", type="biz")
        self.assertEqual(url + "&text=Coffe&lang=ru_RU&type=biz", request)

        y_map: type(YaMaps) = YaMaps("188jasdknl-bfe2-75e456761816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=188jasdknl-bfe2-75e456761816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        request = y_map._generate_request(text="Pokemon", lang="ru_RU", ll="37.618920,55.756994")
        self.assertEqual(url + "&text=Pokemon&lang=ru_RU&ll=37.618920,55.756994", request)

    @async_test
    async def test_async_wait(self):
        """ Тест на открытие сесии с помощью async wait """

        y_map: type(YaMaps) = YaMaps("12b9aefasc-0000-49ae-1233-65ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-0000-49ae-1233-65ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            pass

        y_map: type(YaMaps) = YaMaps("12b9ac-1231-49ae-0000-ab5ed6cb6asa16")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9ac-1231-49ae-0000-ab5ed6cb6asa16"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            pass

        y_map: type(YaMaps) = YaMaps("0000")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=0000"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            pass

        y_map: type(YaMaps) = YaMaps("")
        url: str = "https://search-maps.yandex.ru/v1/?apikey="
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            pass

    @async_test
    async def test_request(self):
        """ Тест на отправку запроса к yandex maps api, функция request """

        y_map: type(YaMaps) = YaMaps("12b9aefasc-0000-49ae-1233-65ecb61816")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9aefasc-0000-49ae-1233-65ecb61816"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            response: dict = await y_map.request(text="Foo", lang="ru_RU")
            self.assertEqual(response['statusCode'], 403)
            self.assertEqual(response['error'], "Forbidden")
            self.assertEqual(response['message'], "Invalid key")

        y_map: type(YaMaps) = YaMaps("12b9ac-1231-49ae-0000-ab5ed6cb6asa16")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9ac-1231-49ae-0000-ab5ed6cb6asa16"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            response: dict = await y_map.request(text="BAR", lang="en_EN")
            self.assertEqual(response['statusCode'], 403)
            self.assertEqual(response['error'], "Forbidden")
            self.assertEqual(response['message'], "Invalid key")

        y_map: type(YaMaps) = YaMaps("0000")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=0000"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            response: dict = await y_map.request(text="BOBEE", lang="ru_RU", type="geo")
            self.assertEqual(response['statusCode'], 403)
            self.assertEqual(response['error'], "Forbidden")
            self.assertEqual(response['message'], "Invalid key")

        y_map: type(YaMaps) = YaMaps("1")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=1"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            response: dict = await y_map.request(text="rr", lang="ru_RU", type="biz", ll="37.6120678,55.75789094")
            self.assertEqual(response['statusCode'], 403)
            self.assertEqual(response['error'], "Forbidden")
            self.assertEqual(response['message'], "Invalid key")


if __name__ == '__main__':
    unittest.main()
