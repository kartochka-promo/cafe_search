
import unittest
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty
from yamaps.yandex_response.feature.company_meta_data.company_meta_data import CompanyMetaData
from yamaps.yandex_response.feature.company_meta_data.hours.hours import Hours


class TestHours(unittest.TestCase):
    """ Класс для тестирования класса Availability """

    def test_init(self):
        """ Тест на инициализацию класса Geometry """
        obj = CompanyMetaData({})
        self.assertEqual(obj.context, {})

        obj = CompanyMetaData(None)
        self.assertEqual(obj.context, None)

        obj = CompanyMetaData(123)
        self.assertEqual(obj.context, 123)

        obj = CompanyMetaData([])
        self.assertEqual(obj.context, [])

        obj = CompanyMetaData(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct_simple_properties(self):
        """ Тест на парсинг простых(одновложенных) свойств """

        obj = CompanyMetaData({'id': '200329884203',
                               'name': 'Area-51',
                               'address': 'Соединённые Штаты Америки, Невада, Линкольн-Каунти',
                               'url': 'http://www.ov.kz/'})

        self.assertEqual(obj.context, {'id': '200329884203',
                                       'name': 'Area-51',
                                       'address': 'Соединённые Штаты Америки, Невада, Линкольн-Каунти',
                                       'url': 'http://www.ov.kz/'})

        self.assertEqual(obj.id, '200329884203')
        self.assertEqual(obj.name, 'Area-51')
        self.assertEqual(obj.address, 'Соединённые Штаты Америки, Невада, Линкольн-Каунти')
        self.assertEqual(obj.url, 'http://www.ov.kz/')

    def test_destruct_categories(self):
        """ Тест на парсинг поля categories """

        obj = CompanyMetaData({'Categories': [
            {'class': 'science', 'name': 'Научно-производственная организация'},
            {'class': 'police', 'name': 'Военкомат'},
            {'class': 'college', 'name': 'Военная, кадетская школа'}
        ]})

        self.assertEqual(obj.context, {'Categories': [
            {'class': 'science', 'name': 'Научно-производственная организация'},
            {'class': 'police', 'name': 'Военкомат'},
            {'class': 'college', 'name': 'Военная, кадетская школа'}
        ]})

        self.assertIs(type(obj.categories), list)
        self.assertEqual(len(obj.categories), 3)

    def test_destruct_phones(self):
        """ Тест на парсинг поля phones """

        obj = CompanyMetaData({'Phones': [
            {'type': 'phone', 'formatted': '+998 71 248 24 00'},
            {'type': 'phone', 'formatted': '+998 71 248 25 21'}
        ]})

        self.assertEqual(obj.context, {'Phones': [
            {'type': 'phone', 'formatted': '+998 71 248 24 00'},
            {'type': 'phone', 'formatted': '+998 71 248 25 21'}
        ]})

        self.assertIs(type(obj.phones), list)
        self.assertEqual(len(obj.phones), 2)

    def test_destruct_hours(self):
        """ Тест на парсинг поля hours """

        obj = CompanyMetaData({'Hours': {'text': 'пн-пт 9:00–18:00, перерыв 13:00–14:00',
                                         'Availabilities': [
                                             {'Intervals': [
                                                 {'from': '09:00:00', 'to': '13:00:00'},
                                                 {'from': '14:00:00', 'to': '18:00:00'}
                                             ],
                                                 'Monday': True, 'Tuesday': True,
                                                 'Wednesday': True, 'Thursday': True,
                                                 'Friday': True
                                             }
                                         ]}
                               })

        self.assertEqual(obj.context, {'Hours': {'text': 'пн-пт 9:00–18:00, перерыв 13:00–14:00',
                                                 'Availabilities': [
                                                     {'Intervals': [
                                                         {'from': '09:00:00', 'to': '13:00:00'},
                                                         {'from': '14:00:00', 'to': '18:00:00'}
                                                     ], 'Monday': True, 'Tuesday': True,
                                                         'Wednesday': True, 'Thursday': True,
                                                         'Friday': True}
                                                 ]}
                                       })

        self.assertIs(type(obj.hours), Hours)
        self.assertEqual(obj.hours.text, 'пн-пт 9:00–18:00, перерыв 13:00–14:00')

    def test_destruct(self):
        obj = CompanyMetaData({'id': '212658931246',
                               'name': 'Алмазарский отдел по делам обороны',
                               'address': 'Узбекистан, Ташкент, Ташкент г., Бабаджанова улица, 14',
                               'Phones': [
                                   {'type': 'phone', 'formatted': '+998 71 248 24 00'},
                                   {'type': 'phone', 'formatted': '+998 71 248 25 21'}
                               ],
                               'Categories': [{'class': 'police', 'name': 'Военкомат'}]
                               })

        self.assertEqual(obj.context, {'id': '212658931246',
                                       'name': 'Алмазарский отдел по делам обороны',
                                       'address': 'Узбекистан, Ташкент, Ташкент г., Бабаджанова улица, 14',
                                       'Phones': [
                                           {'type': 'phone', 'formatted': '+998 71 248 24 00'},
                                           {'type': 'phone', 'formatted': '+998 71 248 25 21'}
                                       ],
                                       'Categories': [{'class': 'police', 'name': 'Военкомат'}]
                                       })

        self.assertEqual(obj.id, '212658931246')
        self.assertEqual(obj.name, 'Алмазарский отдел по делам обороны')
        self.assertEqual(obj.address, 'Узбекистан, Ташкент, Ташкент г., Бабаджанова улица, 14')
        self.assertEqual(obj.url, None)

        self.assertIs(type(obj.categories), list)
        self.assertEqual(len(obj.categories), 1)

        self.assertIs(type(obj.phones), list)
        self.assertEqual(len(obj.phones), 2)
        self.assertIs(obj.hours, None)

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = CompanyMetaData({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as id_context:
            obj_id = obj.id

        id_context.exception("123")
        self.assertEqual(obj.id, "123")

        with self.assertRaises(MissingRequiredProperty) as name_context:
            obj_name = obj.name

        name_context.exception("proper")
        self.assertEqual(obj.name, "proper")

        self.assertEqual(obj.address, None)
        self.assertEqual(obj.url, None)
        self.assertEqual(obj.categories, [])
        self.assertEqual(obj.phones, [])
        self.assertEqual(obj.hours, None)

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = CompanyMetaData({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as id_context:
            obj_id = obj.id

        obj.id = "123"
        self.assertEqual(obj.id, "123")

        with self.assertRaises(MissingRequiredProperty) as name_context:
            obj_name = obj.name

        obj.name = "proper"
        self.assertEqual(obj.name, "proper")

        self.assertEqual(obj.address, None)
        obj.address = "sample string"
        self.assertEqual(obj.address, "sample string")

        self.assertEqual(obj.url, None)
        obj.url = "http://sample_url.com"
        self.assertEqual(obj.url, "http://sample_url.com")

        self.assertEqual(obj.categories, [])
        obj.categories = [
            {'class': 'science', 'name': 'Научно-производственная организация'},
            {'class': 'police', 'name': 'Военкомат'},
            {'class': 'college', 'name': 'Военная, кадетская школа'}
        ]

        self.assertIs(type(obj.categories), list)
        self.assertEqual(len(obj.categories), 3)

        self.assertEqual(obj.phones, [])
        obj.phones = [
            {'type': 'phone', 'formatted': '+998 71 248 24 00'},
            {'type': 'phone', 'formatted': '+998 71 248 25 21'}
        ]

        self.assertIs(type(obj.phones), list)
        self.assertEqual(len(obj.phones), 2)

        self.assertEqual(obj.hours, None)
        obj.hours = {'text': 'пн-пт 9:00–18:00, перерыв 13:00–14:00',
                     'Availabilities': [
                         {'Intervals': [
                             {'from': '09:00:00', 'to': '13:00:00'},
                             {'from': '14:00:00', 'to': '18:00:00'}
                         ],
                             'Monday': True, 'Tuesday': True,
                             'Wednesday': True, 'Thursday': True,
                             'Friday': True
                         }
                     ]}

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = CompanyMetaData({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as id_context:
            obj_id = obj.id

        obj.id = "123"
        self.assertEqual(obj.id, "123")

        with self.assertRaises(MissingRequiredProperty) as name_context:
            obj_name = obj.name

        obj.name = "proper"
        self.assertEqual(obj.name, "proper")

        self.assertEqual(obj.address, None)
        obj.address = "sample string"
        self.assertEqual(obj.address, "sample string")

        self.assertEqual(obj.url, None)
        obj.url = "http://sample_url.com"
        self.assertEqual(obj.url, "http://sample_url.com")

        self.assertEqual(obj.categories, [])
        obj.categories = [
            {'class': 'science', 'name': 'Научно-производственная организация'},
            {'class': 'police', 'name': 'Военкомат'},
            {'class': 'college', 'name': 'Военная, кадетская школа'}
        ]

        self.assertIs(type(obj.categories), list)
        self.assertEqual(len(obj.categories), 3)

        self.assertEqual(obj.phones, [])
        obj.phones = [
            {'type': 'phone', 'formatted': '+998 71 248 24 00'},
            {'type': 'phone', 'formatted': '+998 71 248 25 21'}
        ]

        self.assertIs(type(obj.phones), list)
        self.assertEqual(len(obj.phones), 2)

        self.assertEqual(obj.hours, None)
        obj.hours = {'text': 'пн-пт 9:00–18:00, перерыв 13:00–14:00',
                     'Availabilities': [
                         {'Intervals': [
                             {'from': '09:00:00', 'to': '13:00:00'},
                             {'from': '14:00:00', 'to': '18:00:00'}
                         ],
                             'Monday': True, 'Tuesday': True,
                             'Wednesday': True, 'Thursday': True,
                             'Friday': True
                         }
                     ]}

        del obj.address
        self.assertEqual(obj.address, None)

        del obj.url
        self.assertEqual(obj.url, None)

        del obj.categories
        self.assertEqual(obj.categories, [])

        del obj.phones
        self.assertEqual(obj.phones, [])

        del obj.hours
        self.assertEqual(obj.hours, None)


if __name__ == '__main__':
    unittest.main()