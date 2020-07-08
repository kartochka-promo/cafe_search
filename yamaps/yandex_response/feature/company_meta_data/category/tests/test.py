
import unittest
from ..category import Category
from .....exceptions.exceptions import MissingRequiredProperty


class TestHours(unittest.TestCase):
    """ Класс для тестирования класса Availability """

    def test_init(self):
        """ Тест на инициализацию класса Geometry """
        obj = Category({})
        self.assertEqual(obj.context, {})

        obj = Category(None)
        self.assertEqual(obj.context, None)

        obj = Category(123)
        self.assertEqual(obj.context, 123)

        obj = Category([])
        self.assertEqual(obj.context, [])

        obj = Category(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct(self):
        """ Тест на парсинг полного контекста """

        obj = Category({"class": "шиномойка", "name": "cars"})
        self.assertEqual(obj.context, {"class": "шиномойка", "name": "cars"})

        self.assertEqual(obj.cls, "шиномойка")
        self.assertEqual(obj.name, "cars")

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = Category({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as name_context:
            obj_name = obj.name

        name_context.exception("name context")
        self.assertEqual(obj.name, "name context")
        self.assertEqual(obj.cls, None)

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = Category({})
        self.assertEqual(obj.context, {})

        obj.cls = "some text"
        self.assertEqual(obj.cls, "some text")

        obj.name = "test"
        self.assertEqual(obj.name, "test")

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = Category({})
        self.assertEqual(obj.context, {})

        obj.cls = "some text"
        self.assertEqual(obj.cls, "some text")

        obj.name = "test"
        self.assertEqual(obj.name, "test")

        del obj.name
        with self.assertRaises(MissingRequiredProperty) as name_context:
            obj_name = obj.name

        del obj.cls
        self.assertEqual(obj.cls, None)


if __name__ == '__main__':
    unittest.main()