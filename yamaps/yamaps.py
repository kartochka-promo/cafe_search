import aiohttp
import asyncio


class YaMaps:
    """
    Класс, реализующий обращение к yandex maps api
    https://tech.yandex.ru/maps/geosearch/doc/concepts/request-docpage/
    Пример использования:

    async with YaMaps("12b9aefc-0d5e-49ae-bfe2-75ee6cb61816") as yamap:
        print(await yamap.request(text="Кофе", lang="ru_RU"))
    """

    def __init__(self, key: str) -> None:
        """
        Конструктор класса YaMaps

        :type key: str
        :param key: api ключ для yandex maps
        """
        self._url: str = f'https://search-maps.yandex.ru/v1/?apikey={key}'
        self._session = None

    def _open(self) -> object:
        """
        Protected метод для открытия сессии aiohttp
        Лучше пользоваться async with

        :rtype: obj
        :return: Возвращает экземпляр класса YaMaps
        """
        self._session = aiohttp.ClientSession()
        return self

    async def _close(self) -> None:
        """
        Protected метод для закрытия сессии aiohttp,
        Должен вызываться после завернения работы с YaMaps
        Лучше пользоваться async with

        :rtype: None
        :return: Ничего не возвращает
        """
        await self._session.close()

    async def __aenter__(self) -> object:
        """
        Метод, определяющий, что происходит при вызове async with
        В данном случае происходит открытие сессии aiohttp

        :rtype: obj
        :return: Возвращает экземпляр класса YaMaps
        """
        return self._open()

    async def __aexit__(self, exception_type, exception_value, traceback) -> None:
        """
        Метод, определяющий, что происходит после выхода из тела async with
        В данном случае происходит закрытие сессии aiohttp
        Исключения на данном моменте не обрабатываются и пропускаются выше

        :param exception_type: Тип исключения
        :param exception_value: Значение исключения
        :param traceback: Стек вызовов
        :rtype: None
        :return: Ничего не возвращает
        """
        await self._close()

    def _generate_request(self, **kwargs: str) -> str:
        """
        Метод, генерирующий запрос к yandex maps api

        :type kwargs: Dict[str, str]
        :param kwargs: набор параметров, отсылаемых через get запрос
        где ключ - это имя параметра, значение - это значение параметра
        :rtype: str
        :return: Возвращает запрос к yandex maps api
        """
        request: str = "".join([f"&{key}={value}" for key, value in kwargs.items()])
        return self._url + request

    async def request(self, **kwargs: str) -> dict:
        """
        Метод, реализующий запрос к api yandex maps
        Список всех ключей и возможных параметров и требуемый ответ от сервера
        можно посмотреть здесь https://tech.yandex.ru/maps/geosearch/doc/concepts/request-docpage/

        :type kwargs: Dict[str, str]
        :param kwargs: набор параметров, отсылаемых через get запрос
         где ключ - это имя параметра, значение - это значение параметра
        :rtype: obj
        :return: Возвращает ответ от yandex maps
        """

        request: str = self._generate_request(**kwargs)
        async with self._session.get(request) as resp:
            return await resp.json()


#Testing
# async def test():
#     async with YaMaps("12b9aefc-0d5e-49ae-bfe2-75ee6cb61816") as yamap:
#         print(await yamap.request(text="Военкомат", lang="ru_RU"))
#
# loop = asyncio.get_event_loop()
# result = loop.run_until_complete(test())
