
import unittest
import asyncio
from typing import Any
from asynctest import CoroutineMock, patch

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


class TestYaMaps(unittest.TestCase):
    """
    Класс для тестирования класса YaMaps
    Запуск тестов - coverage3 run --source cafe_search/ -m unittest discover cafe_search -v
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
    @patch('aiohttp.ClientSession.get')
    async def test_request(self, mock):

        context = {
            "type": "FeatureCollection",
            "properties": {
                "ResponseMetaData": {
                    "SearchResponse": {
                        "found": 90,
                        "display": "multiple"
                    },
                    "SearchRequest": {
                        "request": "Военкомат",
                        "skip": 0,
                        "results": 10,
                        "boundedBy": [
                            [
                                37.048427,
                                55.43644866
                            ],
                            [
                                38.175903,
                                56.04690174
                            ]
                        ]
                    }
                }
            },
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            -115.814413,
                            37.239815
                        ]
                    },
                    "properties": {
                        "name": "Area-51",
                        "description": "Соединённые Штаты Америки, Невада, Линкольн-Каунти",
                        "boundedBy": [
                            [
                                -116.738362,
                                36.31643061
                            ],
                            [
                                -114.890464,
                                38.15193077
                            ]
                        ],
                        "CompanyMetaData": {
                            "id": "200329884203",
                            "name": "Area-51",
                            "address": "Соединённые Штаты Америки, Невада, Линкольн-Каунти",
                            "Categories": [
                                {
                                    "class": "science",
                                    "name": "Научно-производственная организация"
                                },
                                {
                                    "class": "police",
                                    "name": "Военкомат"
                                },
                                {
                                    "class": "college",
                                    "name": "Военная, кадетская школа"
                                }
                            ]
                        }
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            69.22529,
                            41.385214
                        ]
                    },
                    "properties": {
                        "name": "Алмазарский отдел по делам обороны",
                        "description": "пр. Бабаджанова, 14, Ташкент, Узбекистан",
                        "boundedBy": [
                            [
                                69.2211845,
                                41.38212193
                            ],
                            [
                                69.2293955,
                                41.38830593
                            ]
                        ],
                        "CompanyMetaData": {
                            "id": "212658931246",
                            "name": "Алмазарский отдел по делам обороны",
                            "address": "Узбекистан, Ташкент, Ташкент г., Бабаджанова улица, 14",
                            "Phones": [
                                {
                                    "type": "phone",
                                    "formatted": "+998 71 248 24 00"
                                },
                                {
                                    "type": "phone",
                                    "formatted": "+998 71 248 25 21"
                                }
                            ],
                            "Categories": [
                                {
                                    "class": "police",
                                    "name": "Военкомат"
                                }
                            ]
                        }
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            71.424889,
                            51.16356
                        ]
                    },
                    "properties": {
                        "name": "Департамент по делам обороны г. Нур-Султан",
                        "description": "ул. Мухтара Ауэзова, 5А, Нур-Султан (Астана), Казахстан",
                        "boundedBy": [
                            [
                                71.4207835,
                                51.16097893
                            ],
                            [
                                71.4289945,
                                51.16614093
                            ]
                        ],
                        "CompanyMetaData": {
                            "id": "1019820168",
                            "name": "Департамент по делам обороны г. Нур-Султан",
                            "address": "Казахстан, Нур-Султан (Астана), улица Мухтара Ауэзова, 5А",
                            "url": "http://www.mod.gov.kz/",
                            "Phones": [
                                {
                                    "type": "phone",
                                    "formatted": "+7 (7172) 32-80-76"
                                },
                                {
                                    "type": "phone",
                                    "formatted": "+7 (7172) 32-70-80"
                                },
                                {
                                    "type": "phone",
                                    "formatted": "+7 (7172) 72-18-33"
                                }
                            ],
                            "Categories": [
                                {
                                    "class": "police",
                                    "name": "Военкомат"
                                }
                            ],
                            "Hours": {
                                "text": "пн-пт 9:00–18:00, перерыв 13:00–14:00",
                                "Availabilities": [
                                    {
                                        "Intervals": [
                                            {
                                                "from": "09:00:00",
                                                "to": "13:00:00"
                                            },
                                            {
                                                "from": "14:00:00",
                                                "to": "18:00:00"
                                            }
                                        ],
                                        "Monday": True,
                                        "Tuesday": True,
                                        "Wednesday": True,
                                        "Thursday": True,
                                        "Friday": True
                                    }
                                ]
                            }
                        }
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            69.261491,
                            41.338014
                        ]
                    },
                    "properties": {
                        "name": "Военкомат Шаихантаурского района",
                        "description": "ул. Тахтапуль, 45, Ташкент, Узбекистан",
                        "boundedBy": [
                            [
                                69.257386,
                                41.33491993
                            ],
                            [
                                69.265596,
                                41.34110793
                            ]
                        ],
                        "CompanyMetaData": {
                            "id": "3841137525",
                            "name": "Военкомат Шаихантаурского района",
                            "address": "Узбекистан, Ташкент, улица Тахтапуль, 45",
                            "Categories": [
                                {
                                    "class": "police",
                                    "name": "Военкомат"
                                }
                            ],
                            "Hours": {
                                "text": "пн-пт 9:00–18:00, перерыв 13:00–14:00",
                                "Availabilities": [
                                    {
                                        "Intervals": [
                                            {
                                                "from": "09:00:00",
                                                "to": "13:00:00"
                                            },
                                            {
                                                "from": "14:00:00",
                                                "to": "18:00:00"
                                            }
                                        ],
                                        "Monday": True,
                                        "Tuesday": True,
                                        "Wednesday": True,
                                        "Thursday": True,
                                        "Friday": True
                                    }
                                ]
                            }
                        }
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            76.629355,
                            43.199431
                        ]
                    },
                    "properties": {
                        "name": "Карасайский Районный Военкомат",
                        "description": "Казахстан, Алматинская область, Карасайский район, Каскелен",
                        "boundedBy": [
                            [
                                76.587462,
                                43.15568322
                            ],
                            [
                                76.671248,
                                43.24314722
                            ]
                        ],
                        "CompanyMetaData": {
                            "id": "205361912483",
                            "name": "Карасайский Районный Военкомат",
                            "address": "Казахстан, Алматинская область, Карасайский район, Каскелен",
                            "Categories": [
                                {
                                    "class": "police",
                                    "name": "Военкомат"
                                }
                            ]
                        }
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            71.434149,
                            51.167822
                        ]
                    },
                    "properties": {
                        "name": "Управление по делам обороны Алматинского района",
                        "description": "ул. Иманбаевой, 16, Нур-Султан (Астана), Казахстан",
                        "boundedBy": [
                            [
                                71.430044,
                                51.16524093
                            ],
                            [
                                71.438254,
                                51.17040293
                            ]
                        ],
                        "CompanyMetaData": {
                            "id": "93984160554",
                            "name": "Управление по делам обороны Алматинского района",
                            "address": "Казахстан, Нур-Султан (Астана), улица Иманбаевой, 16",
                            "url": "http://mod.gov.kz/",
                            "Phones": [
                                {
                                    "type": "phone",
                                    "formatted": "+7 (8172) 20-21-13"
                                }
                            ],
                            "Categories": [
                                {
                                    "class": "police",
                                    "name": "Военкомат"
                                },
                                {
                                    "class": "government",
                                    "name": "Министерства, ведомства, государственные службы"
                                }
                            ],
                            "Hours": {
                                "text": "пн-пт 9:00–18:00, перерыв 13:00–14:00",
                                "Availabilities": [
                                    {
                                        "Intervals": [
                                            {
                                                "from": "09:00:00",
                                                "to": "13:00:00"
                                            },
                                            {
                                                "from": "14:00:00",
                                                "to": "18:00:00"
                                            }
                                        ],
                                        "Monday": True,
                                        "Tuesday": True,
                                        "Wednesday": True,
                                        "Thursday": True,
                                        "Friday": True
                                    }
                                ]
                            }
                        }
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            76.851154,
                            43.224864
                        ]
                    },
                    "properties": {
                        "name": "Управление по делам обороны Ауэзовского района",
                        "description": "41А, 3-й микрорайон, Алматы, Казахстан",
                        "boundedBy": [
                            [
                                76.847049,
                                43.22186193
                            ],
                            [
                                76.855259,
                                43.22786593
                            ]
                        ],
                        "CompanyMetaData": {
                            "id": "30338088265",
                            "name": "Управление по делам обороны Ауэзовского района",
                            "address": "Казахстан, Алматы, 3-й микрорайон, 41А",
                            "Phones": [
                                {
                                    "type": "phone",
                                    "formatted": "+7 (727) 381-56-49"
                                }
                            ],
                            "Categories": [
                                {
                                    "class": "police",
                                    "name": "Военкомат"
                                }
                            ],
                            "Hours": {
                                "text": "пн-пт 9:00–18:00, перерыв 13:00–14:00",
                                "Availabilities": [
                                    {
                                        "Intervals": [
                                            {
                                                "from": "09:00:00",
                                                "to": "13:00:00"
                                            },
                                            {
                                                "from": "14:00:00",
                                                "to": "18:00:00"
                                            }
                                        ],
                                        "Monday": True,
                                        "Tuesday": True,
                                        "Wednesday": True,
                                        "Thursday": True,
                                        "Friday": True
                                    }
                                ]
                            }
                        }
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            76.914882,
                            43.244434
                        ]
                    },
                    "properties": {
                        "name": "Управление по делам обороны Алмалинского района",
                        "description": "ул. Шевченко, 131, Алматы, Казахстан",
                        "boundedBy": [
                            [
                                76.9107765,
                                43.24143243
                            ],
                            [
                                76.9189875,
                                43.24743543
                            ]
                        ],
                        "CompanyMetaData": {
                            "id": "1008673735",
                            "name": "Управление по делам обороны Алмалинского района",
                            "address": "Казахстан, Алматы, улица Шевченко, 131",
                            "Phones": [
                                {
                                    "type": "phone",
                                    "formatted": "+7 (727) 395-84-50"
                                },
                                {
                                    "type": "phone",
                                    "formatted": "+7 (727) 395-84-51"
                                },
                                {
                                    "type": "phone",
                                    "formatted": "+7 (727) 395-84-48"
                                },
                                {
                                    "type": "phone",
                                    "formatted": "+7 (727) 395-84-46"
                                },
                                {
                                    "type": "phone",
                                    "formatted": "+7 (727) 395-84-47"
                                }
                            ],
                            "Categories": [
                                {
                                    "class": "police",
                                    "name": "Военкомат"
                                }
                            ],
                            "Hours": {
                                "text": "пн-пт 9:00–18:00, перерыв 13:00–14:00; сб 9:00–13:00",
                                "Availabilities": [
                                    {
                                        "Intervals": [
                                            {
                                                "from": "09:00:00",
                                                "to": "13:00:00"
                                            },
                                            {
                                                "from": "14:00:00",
                                                "to": "18:00:00"
                                            }
                                        ],
                                        "Monday": True,
                                        "Tuesday": True,
                                        "Wednesday": True,
                                        "Thursday": True,
                                        "Friday": True
                                    },
                                    {
                                        "Intervals": [
                                            {
                                                "from": "09:00:00",
                                                "to": "13:00:00"
                                            }
                                        ],
                                        "Saturday": True
                                    }
                                ]
                            }
                        }
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            80.254453,
                            50.413658
                        ]
                    },
                    "properties": {
                        "name": "Военный комиссариат",
                        "description": "ул. Валиханова, 108, Семей, Казахстан",
                        "boundedBy": [
                            [
                                80.250348,
                                50.41103493
                            ],
                            [
                                80.258558,
                                50.41628093
                            ]
                        ],
                        "CompanyMetaData": {
                            "id": "119606639838",
                            "name": "Военный комиссариат",
                            "address": "Казахстан, Восточно-Казахстанская область, Семей, улица Валиханова, 108",
                            "Categories": [
                                {
                                    "class": "police",
                                    "name": "Военкомат"
                                }
                            ]
                        }
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            69.178725,
                            41.310426
                        ]
                    },
                    "properties": {
                        "name": "Учтепинский Отдел по Делам Обороны",
                        "description": "ул. Гулома Зафари, 16А, Ташкент, Узбекистан",
                        "boundedBy": [
                            [
                                69.1746195,
                                41.30733093
                            ],
                            [
                                69.1828305,
                                41.31352093
                            ]
                        ],
                        "CompanyMetaData": {
                            "id": "202609170421",
                            "name": "Учтепинский Отдел по Делам Обороны",
                            "address": "Узбекистан, Ташкент, улица Зафари, 16А",
                            "Phones": [
                                {
                                    "type": "phone",
                                    "formatted": "+998 71 228 60 29"
                                },
                                {
                                    "type": "phone",
                                    "formatted": "+998 71 247 15 26"
                                },
                                {
                                    "type": "phone",
                                    "formatted": "+371  712 28 60 29"
                                }
                            ],
                            "Categories": [
                                {
                                    "class": "police",
                                    "name": "Военкомат"
                                }
                            ],
                            "Hours": {
                                "text": "пн-пт 9:00–17:00, перерыв 13:00–14:00",
                                "Availabilities": [
                                    {
                                        "Intervals": [
                                            {
                                                "from": "09:00:00",
                                                "to": "13:00:00"
                                            },
                                            {
                                                "from": "14:00:00",
                                                "to": "17:00:00"
                                            }
                                        ],
                                        "Monday": True,
                                        "Tuesday": True,
                                        "Wednesday": True,
                                        "Thursday": True,
                                        "Friday": True
                                    }
                                ]
                            }
                        }
                    }
                }
            ]
        }

        mock.return_value.__aenter__.return_value.json = CoroutineMock(side_effect=[context])
        y_map: type(YaMaps) = YaMaps("12b9ac-1231-49ae-0000-ab5ed6cb6asa16")
        url: str = "https://search-maps.yandex.ru/v1/?apikey=12b9ac-1231-49ae-0000-ab5ed6cb6asa16"
        self.assertEqual(y_map._url, url)
        self.assertEqual(y_map._session, None)
        async with y_map as _:
            y_response = await y_map.request(text="Кофейни", lang="ru_RU", type="biz", rspn="1", results="500")
            self.assertEqual(y_response.context, context)


if __name__ == '__main__':
    unittest.main()
