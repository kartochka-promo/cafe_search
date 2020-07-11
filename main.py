
import redis
import asyncio
from yamaps.yamaps import YaMaps
from crawler.crawler import Crawler


async def main():
    async with YaMaps("634e8c51-ce37-4e01-a8a9-14607f757ca3") as yamap:

        redis_db_0 = redis.StrictRedis(host='localhost', port=6379, db=0)
        redis_db_1 = redis.StrictRedis(host='localhost', port=6379, db=1)

        request_params = {
            "text": "Кофейни",
            "lang": "ru_RU",
            "type": "biz",
            "rspn": "1",
            "results": "500"
        }

        bbox = [[37.048427, 55.43644866], [38.175903, 56.04690174]]
        ya_crawler = Crawler(redis_db_0, redis_db_1, yamap, request_params, bbox)

        await ya_crawler.run()
        new_obj = await ya_crawler.get_new_objects_list()
        for obj in new_obj:
            print(obj.company_meta_data.name, obj.company_meta_data.address)

loop = asyncio.get_event_loop()
result = loop.run_until_complete(main())