
import aiohttp
import asyncio


class YaMaps:
    """ Конструктор класса YaMaps
        key(stirng) - ваш api ключ для yandex maps
    """
    def __init__(self, key: str) -> None:
        self.url = f'https://search-maps.yandex.ru/v1/?apikey={key}'
        self.session = None

    """ Protected метод для открытия сессии aiohttp
        Лучше использовать async with
    """
    def _open(self) -> None:
        self.session = aiohttp.ClientSession()

    """ Protected метод для закрытия сессии aiohttp,
        Должен вызываться после завернения работы с YaMaps
        Лучше использовать async with
    """
    async def _close(self) -> None:
        await self.session.close()

    """ Метод, определяющий, что происходит при вызове async with 
        В данном случае происходит открытие сессии aiohttp    
    """
    async def __aenter__(self) -> object:
        self._open()
        return self

    """ Метод, определяющий, что происходит после выхода из тела async with 
        В данном случае происходит закрытие сессии aiohttp    
        Исключения на данном моменте не обрабатываются и пропускаются выше
    """
    async def __aexit__(self, exception_type, exception_value, traceback) -> None:
        await self._close()

    """ Метод, реализующий запрос к api yandex maps
        kwargs(dict) - набор параметров, отсылаемых через get запрос
        Где ключ - это имя параметра, значение - это значение параметра
        Список всех ключей и возможных параметров и требуемый ответ от сервера 
        можно посмотреть здесь https://tech.yandex.ru/maps/geosearch/doc/concepts/request-docpage/    
    """
    async def request(self, **kwargs: dict) -> object:
        request = "".join([f"&{key}={value}" for key, value in kwargs.items()])
        async with self.session.get(self.url + request) as resp:
            return await resp.json()


# Testing
async def test():
    async with YaMaps("12b9aefc-0d5e-49ae-bfe2-75ee6cb61816") as yamap:
        print(await yamap.request(text="Кофе", lang="ru_RU"))

loop = asyncio.get_event_loop()
result = loop.run_until_complete(test())
