#
# import pickle
# import redis
# import asyncio
# from yamaps.yamaps import YaMaps
#
#
# # r = redis.StrictRedis(host='localhost', port=6379, db=0)
# # obj = a()
# # pickled_object = pickle.dumps(obj)
# # r.set('some_key', pickled_object)
# # unpacked_object = pickle.loads(r.get('some_key'))
#
#
# async def test():
#     for i in range(100):
#         async with YaMaps("12b9aefc-0d5e-49ae-bfe2-75ee6cb61816") as yamap:
#             ya_response = await yamap.request(text="Кофейни Москва", lang="ru_RU",
#                                               type="biz",
#                                               bbox="37.048427,55.43644866~38.175903,56.04690174",
#                                               results="500",
#                                               #skip="1000"
#                                               )
#             #print(ya_response.context)
#             print(i)
#
# loop = asyncio.get_event_loop()
# result = loop.run_until_complete(test())