import aiohttp
import asyncio


class YaMaps:
    def __init__(self, key):
        self.url = f'https://search-maps.yandex.ru/v1/?apikey={key}'
        self.session = None

    def _open(self):
        self.session = aiohttp.ClientSession()

    async def _close(self):
        await self.session.close()

    async def __aenter__(self):
        self._open()
        return self

    async def __aexit__(self, exception_type, exception_value, traceback):
        await self._close()

    async def request(self, **kwargs):
        request = "".join([f"&{key}={value}" for key, value in kwargs.items()])
        async with self.session.get(self.url + request) as resp:
            return await resp.json()


# Testing
async def test():
    async with YaMaps("12b9aefc-0d5e-49ae-bfe2-75ee6cb61816") as yamap:
        print(await yamap.request(text="Кофе", lang="ru_RU"))


loop = asyncio.get_event_loop()
result = loop.run_until_complete(test())