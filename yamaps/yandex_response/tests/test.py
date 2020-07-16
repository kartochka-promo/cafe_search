
import unittest

from yamaps.yandex_response.yandex_response import YandexResponse
from yamaps.yandex_response.response_meta_data.response_meta_data import ResponseMetaData
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty


class TestYandexResponse(unittest.TestCase):
    """ Класс для тестирования класса YandexResponse """

    def test_init(self):
        """ Тест на инициализацию класса YandexResponse """
        obj = YandexResponse({})
        self.assertEqual(obj.context, {})

        obj = YandexResponse(None)
        self.assertEqual(obj.context, None)

        obj = YandexResponse(123)
        self.assertEqual(obj.context, 123)

        obj = YandexResponse([])
        self.assertEqual(obj.context, [])

        obj = YandexResponse(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct_response_meta_data(self):
        """ Тест на парсинг свойства ResponseMetaData """

        obj = YandexResponse({
            'type': 'FeatureCollection',
            'properties': {
                'ResponseMetaData': {
                    'SearchResponse': {
                        'found': 90,
                        'display': 'multiple'
                    }, 'SearchRequest': {
                        'request': 'Военкомат',
                        'skip': 0,
                        'results': 10,
                        'boundedBy': [[37.048427, 55.43644866], [38.175903, 56.04690174]]
                    }
                }
            }
        })

        self.assertEqual(obj.context, {
            'type': 'FeatureCollection',
            'properties': {
                'ResponseMetaData': {
                    'SearchResponse': {
                        'found': 90,
                        'display': 'multiple'
                    }, 'SearchRequest': {
                        'request': 'Военкомат',
                        'skip': 0,
                        'results': 10,
                        'boundedBy': [[37.048427, 55.43644866], [38.175903, 56.04690174]]
                    }
                }
            }
        })

        self.assertIs(type(obj.response_meta_data), ResponseMetaData)

    def test_destruct_features(self):
        """ Тест на парсинг свойства features """

        obj = YandexResponse({'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [-115.814413, 37.239815]
                }, 'properties': {
                    'name': 'Area-51',
                    'description': 'Соединённые Штаты Америки, Невада, Линкольн-Каунти',
                    'boundedBy': [[-116.738362, 36.31643061], [-114.890464, 38.15193077]],
                    'CompanyMetaData': {
                        'id': '200329884203',
                        'name': 'Area-51',
                        'address': 'Соединённые Штаты Америки, Невада, Линкольн-Каунти',
                        'Categories': [
                            {'class': 'science', 'name': 'Научно-производственная организация'},
                            {'class': 'police', 'name': 'Военкомат'},
                            {'class': 'college', 'name': 'Военная, кадетская школа'}
                        ]
                    }
                }
            },
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [69.22529, 41.385214]
                }, 'properties': {
                    'name': 'Алмазарский отдел по делам обороны',
                    'description': 'пр. Бабаджанова, 14, Ташкент, Узбекистан',
                    'boundedBy': [[69.2211845, 41.38212193], [69.2293955, 41.38830593]],
                    'CompanyMetaData': {
                        'id': '212658931246',
                        'name': 'Алмазарский отдел по делам обороны',
                        'address': 'Узбекистан, Ташкент, Ташкент г., Бабаджанова улица, 14',
                        'Phones': [
                            {'type': 'phone', 'formatted': '+998 71 248 24 00'},
                            {'type': 'phone', 'formatted': '+998 71 248 25 21'}
                        ],
                        'Categories': [{'class': 'police', 'name': 'Военкомат'}]
                    }
                }
            }]})

        self.assertIs(type(obj.features), list)
        self.assertEqual(len(obj.features), 2)

    def test_destruct(self):
        """ Тест на парсинг полного контекста """

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

        obj = YandexResponse(context)
        self.assertEqual(obj.context, context)
        self.assertIs(type(obj.response_meta_data), ResponseMetaData)
        self.assertIs(type(obj.features), list)
        self.assertEqual(len(obj.features), 10)

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = YandexResponse({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as response_meta_data_context:
            obj_response_meta_data = obj.response_meta_data

        with self.assertRaises(MissingRequiredProperty) as features_context:
            obj_features = obj.features

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = YandexResponse({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as response_meta_data_context:
            obj_response_meta_data = obj.response_meta_data

        obj.response_meta_data = {}
        self.assertIs(type(obj.response_meta_data), ResponseMetaData)

        with self.assertRaises(MissingRequiredProperty) as features_context:
            obj_features = obj.features

        obj.features = [{}, {}]
        self.assertIs(type(obj.features), list)
        self.assertEqual(len(obj.features), 2)

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = YandexResponse({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as response_meta_data_context:
            obj_response_meta_data = obj.response_meta_data

        obj.response_meta_data = {}
        self.assertIs(type(obj.response_meta_data), ResponseMetaData)

        with self.assertRaises(MissingRequiredProperty) as features_context:
            obj_features = obj.features

        obj.features = [{}, {}]
        self.assertIs(type(obj.features), list)
        self.assertEqual(len(obj.features), 2)

        del obj.response_meta_data
        with self.assertRaises(MissingRequiredProperty) as response_meta_data_context:
            obj_response_meta_data = obj.response_meta_data

        del obj.features
        with self.assertRaises(MissingRequiredProperty) as features_context:
            obj_features = obj.features


if __name__ == '__main__':
    unittest.main()
