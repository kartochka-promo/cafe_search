
from ..geometry import Geometry
from ....exceptions.exceptions import MissingRequiredProperty

import unittest
import numpy as np


class TestGeometry(unittest.TestCase):
    """ Класс для тестирования класса Geometry """

    def test_init(self):
        """ Тест на инициализацию класса Geometry """
        obj = Geometry({})
        self.assertEqual(obj.context, {})

        obj = Geometry(None)
        self.assertEqual(obj.context, None)

        obj = Geometry(123)
        self.assertEqual(obj.context, 123)

        obj = Geometry([])
        self.assertEqual(obj.context, [])

        obj = Geometry(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct_type(self):
        """ Тест на парсинг поля type """

        obj = Geometry({"type": "point"})
        self.assertEqual(obj.context, {"type": "point"})
        self.assertEqual(obj.type, "point")

    def test_destruct_coordinates(self):
        """ Тест на парсинг поля coordinates """

        obj = Geometry({"coordinates": [12312.12312, 871920.12312]})
        self.assertEqual(obj.context, {"coordinates": [12312.12312, 871920.12312]})
        self.assertEqual(obj.coordinates[0], 12312.12312)
        self.assertEqual(obj.coordinates[1], 871920.12312)

    def test_destruct(self):
        """ Тест на парсинг полного контекста """

        obj = Geometry({"type":"poper", "coordinates": [112.112, 2]})
        self.assertEqual(obj.context, {"type":"poper", "coordinates": [112.112, 2]})
        self.assertEqual(obj.type, "poper")
        self.assertEqual(obj.coordinates[0], 112.112)
        self.assertEqual(obj.coordinates[1], 2)

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = Geometry({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as type_context:
            obj_type = obj.type

        type_context.exception("point")
        self.assertEqual(obj.type, "point")

        with self.assertRaises(MissingRequiredProperty) as coordinates_context:
            obj_coordinates = obj.coordinates

        coordinates_context.exception([1.12312, 2.12312])
        self.assertIs(type(obj.coordinates), np.ndarray)
        self.assertEqual(obj.coordinates[0], 1.12312)
        self.assertEqual(obj.coordinates[1], 2.12312)

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = Geometry({})
        self.assertEqual(obj.context, {})

        obj.type = "point"
        self.assertEqual(obj.type, "point")

        obj.coordinates = [1231.12312, 76890.123]
        self.assertEqual(obj.coordinates[0], 1231.12312)
        self.assertEqual(obj.coordinates[1], 76890.123)

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = Geometry({})
        self.assertEqual(obj.context, {})

        obj.type = "point"
        self.assertEqual(obj.type, "point")

        obj.coordinates = [1231.12312, 76890.123]
        self.assertEqual(obj.coordinates[0], 1231.12312)
        self.assertEqual(obj.coordinates[1], 76890.123)

        del obj.type
        with self.assertRaises(MissingRequiredProperty) as type_context:
            obj_type = obj.type

        del obj.coordinates
        with self.assertRaises(MissingRequiredProperty) as coordinates_context:
            obj_coordinates = obj.coordinates


if __name__ == '__main__':
    unittest.main()