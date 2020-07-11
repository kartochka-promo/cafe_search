
import unittest
from ...exceptions.exceptions import MissingRequiredProperty
from ..feature import Feature
from ..company_meta_data.company_meta_data import CompanyMetaData
from ..geometry.geometry import Geometry


class TestFeature(unittest.TestCase):
    """ Класс для тестирования класса Feature """

    def test_init(self):
        """ Тест на инициализацию класса Feature """
        obj = Feature({})
        self.assertEqual(obj.context, {})

        obj = Feature(None)
        self.assertEqual(obj.context, None)

        obj = Feature(123)
        self.assertEqual(obj.context, 123)

        obj = Feature([])
        self.assertEqual(obj.context, [])

        obj = Feature(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct_simple_properties(self):
        """ Тест на парсинг простых(не вложенных) свойств """

        obj = Feature({'properties': {'name': 'Департамент по делам обороны г. Нур-Султан',
                                      'description': 'ул. Мухтара Ауэзова, 5А, Нур-Султан (Астана), Казахстан'}})

        self.assertEqual(obj.context, {'properties':
                                           {'name': 'Департамент по делам обороны г. Нур-Султан',
                                            'description': 'ул. Мухтара Ауэзова, 5А, Нур-Султан (Астана), Казахстан'}
                                       })

        self.assertEqual(obj.name, 'Департамент по делам обороны г. Нур-Султан')
        self.assertEqual(obj.description, 'ул. Мухтара Ауэзова, 5А, Нур-Султан (Астана), Казахстан')

    def test_destruct_company_meta_data(self):
        """ Тест на парсинг свойства CompanyMetaData """

        obj = Feature({'properties':
                           {'CompanyMetaData':
                                {'id': '212658931246',
                                 'name': 'Алмазарский отдел по делам обороны',
                                 'address': 'Узбекистан, Ташкент, Ташкент г., Бабаджанова улица, 14',
                                 'Phones': [
                                     {'type': 'phone', 'formatted': '+998 71 248 24 00'},
                                     {'type': 'phone', 'formatted': '+998 71 248 25 21'}
                                 ],
                                 'Categories': [
                                     {'class': 'police', 'name': 'Военкомат'}
                                 ]}
                            }
                       })

        self.assertEqual(obj.context, {'properties':
                                           {'CompanyMetaData':
                                                {'id': '212658931246',
                                                 'name': 'Алмазарский отдел по делам обороны',
                                                 'address': 'Узбекистан, Ташкент, Ташкент г., Бабаджанова улица, 14',
                                                 'Phones': [
                                                     {'type': 'phone', 'formatted': '+998 71 248 24 00'},
                                                     {'type': 'phone', 'formatted': '+998 71 248 25 21'}
                                                 ],
                                                 'Categories': [
                                                     {'class': 'police', 'name': 'Военкомат'}
                                                 ]}
                                           }
                                       })

        self.assertIs(type(obj.company_meta_data), CompanyMetaData)

    def test_destruct_geometry(self):
        """ Тест на парсинг свойства geometry """

        obj = Feature({'geometry': {'type': 'Point', 'coordinates': [-115.814413, 37.239815]}})
        self.assertEqual(obj.context, {'geometry': {'type': 'Point', 'coordinates': [-115.814413, 37.239815]}})
        self.assertIs(type(obj.geometry), Geometry)

    def test_destruct(self):
        """ Тест на парсинг полного контекста """

        obj = Feature({'type': 'Feature',
                       'geometry': {
                           'type': 'Point',
                           'coordinates': [-115.814413, 37.239815]
                       }, 'properties':
                           {'name': 'Area-51',
                            'description': 'Соединённые Штаты Америки, Невада, Линкольн-Каунти',
                            'boundedBy': [[-116.738362, 36.31643061], [-114.890464, 38.15193077]],
                            'CompanyMetaData':{
                                'id': '200329884203',
                                'name': 'Area-51',
                                'address': 'Соединённые Штаты Америки, Невада, Линкольн-Каунти',
                                'Categories': [
                                    {'class': 'science', 'name': 'Научно-производственная организация'},
                                    {'class': 'police', 'name': 'Военкомат'},
                                    {'class': 'college', 'name': 'Военная, кадетская школа'}
                                ]
                            }}
                       })

        self.assertEqual(obj.context, {'type': 'Feature',
                                       'geometry': {
                                           'type': 'Point',
                                           'coordinates': [-115.814413, 37.239815]
                                       }, 'properties':
                                           {'name': 'Area-51',
                                            'description': 'Соединённые Штаты Америки, Невада, Линкольн-Каунти',
                                            'boundedBy': [[-116.738362, 36.31643061], [-114.890464, 38.15193077]],
                                            'CompanyMetaData':{
                                                'id': '200329884203',
                                                'name': 'Area-51',
                                                'address': 'Соединённые Штаты Америки, Невада, Линкольн-Каунти',
                                                'Categories': [
                                                    {'class': 'science', 'name': 'Научно-производственная организация'},
                                                    {'class': 'police', 'name': 'Военкомат'},
                                                    {'class': 'college', 'name': 'Военная, кадетская школа'}
                                                ]
                                            }}
                                       })

        self.assertEqual(obj.name, 'Area-51')
        self.assertEqual(obj.description, 'Соединённые Штаты Америки, Невада, Линкольн-Каунти')
        self.assertIs(type(obj.company_meta_data), CompanyMetaData)
        self.assertIs(type(obj.geometry), Geometry)

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = Feature({})
        self.assertEqual(obj.context, {})

        self.assertEqual(obj.name, None)
        self.assertEqual(obj.description, None)
        self.assertEqual(obj.company_meta_data, None)

        with self.assertRaises(MissingRequiredProperty) as geometry_context:
            obj_geometry = obj.geometry

        geometry_context.exception({})
        self.assertIs(type(obj.geometry), Geometry)

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = Feature({})
        self.assertEqual(obj.context, {})

        self.assertEqual(obj.name, None)
        obj.name = "test"
        self.assertIs(obj.name, "test")

        self.assertEqual(obj.description, None)
        obj.description = "description"
        self.assertEqual(obj.description, "description")

        self.assertEqual(obj.company_meta_data, None)
        obj.company_meta_data = {}
        self.assertIs(type(obj.company_meta_data), CompanyMetaData)

        with self.assertRaises(MissingRequiredProperty) as geometry_context:
            obj_geometry = obj.geometry

        geometry_context.exception({})
        self.assertIs(type(obj.geometry), Geometry)

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = Feature({})
        self.assertEqual(obj.context, {})

        self.assertEqual(obj.name, None)
        obj.name = "test"
        self.assertIs(obj.name, "test")

        self.assertEqual(obj.description, None)
        obj.description = "description"
        self.assertEqual(obj.description, "description")

        self.assertEqual(obj.company_meta_data, None)
        obj.company_meta_data = {}
        self.assertIs(type(obj.company_meta_data), CompanyMetaData)

        with self.assertRaises(MissingRequiredProperty) as geometry_context:
            obj_geometry = obj.geometry

        geometry_context.exception({})
        self.assertIs(type(obj.geometry), Geometry)

        del obj.name
        self.assertEqual(obj.name, None)

        del obj.description
        self.assertEqual(obj.description, None)

        del obj.company_meta_data
        self.assertEqual(obj.company_meta_data, None)

        del obj.geometry
        with self.assertRaises(MissingRequiredProperty) as geometry_context:
            obj_geometry = obj.geometry


if __name__ == '__main__':
    unittest.main()