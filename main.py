
import redis
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from random import randrange

from yamaps.yamaps import YaMaps
from crawler.crawler import Crawler


redis_db_0 = redis.StrictRedis(host='localhost', port=6379, db=0)
ya_api_key = "your yandex api key here"
request_params = {
            "text": "Кофейни",
            "lang": "ru_RU",
            "type": "biz",
            "rspn": "1",
            "results": "500"
        }

bbox = [[37.048427, 55.43644866], [38.175903, 56.04690174]]
nice_answers = ["it was something",
                "It was complicated",
                "it was easy",
                "I didn’t even get tired",
                "If you want, we can repeat",
                "Damn I got it, I’m chocolate",
                "Stop, I realized that I was a toaster",
                "Can the server be more powerful",
                "Thanks for waiting",
                "I'm sorry I'm so slow",
                "I love potatoes and you?"]


telegram_token = "BOT TOKEN HERE"
bot = Bot(token=telegram_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! \n"
                        "I'm MlgPotatorBot ;) \n "
                        "Some commands for you: \n "
                        "/run - use to start searching \n "
                        "/clear - use to clear data")


@dp.message_handler(commands=['clear'])
async def send_clear(message: types.Message):
    async with YaMaps(ya_api_key) as yamap:
        redis_db_0.flushdb()
        ya_crawler = Crawler(redis_db_0, yamap, request_params, bbox)
        await ya_crawler.run()

    await message.reply("OK! \n"
                        "It is now clear \n")


@dp.message_handler(commands=['run'])
async def send_run(message: types.Message):
    async with YaMaps(ya_api_key) as yamap:
        ya_crawler = Crawler(redis_db_0, yamap, request_params, bbox)

        await ya_crawler.run()
        new_objects = await ya_crawler.get_new_objects_list()

        if type(new_objects) == list and len(new_objects) > 0:
            await message.reply("Yay! \n"
                                "I am find something.\n")

        futures = [message.reply(f"Name: {obj.company_meta_data.name}\n"
                                 f"Address: {obj.company_meta_data.address}\n"
                                 f"Url: {obj.company_meta_data.url}") for obj in new_objects]

        await asyncio.gather(*futures)
        await message.reply(nice_answers[randrange(11)])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
