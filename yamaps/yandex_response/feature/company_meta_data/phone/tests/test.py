
from yamaps.yandex_response.feature.company_meta_data.phone.phone import Phone
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty
import unittest


class TestGeometry(unittest.TestCase):
    """ Класс для тестирования класса Geometry """

    def test_init(self):
        """ Тест на инициализацию класса Geometry """
        obj = Phone({})
        self.assertEqual(obj.context, {})

        obj = Phone(None)
        self.assertEqual(obj.context, None)

        obj = Phone(123)
        self.assertEqual(obj.context, 123)

        obj = Phone([])
        self.assertEqual(obj.context, [])

        obj = Phone(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct_type(self):
        """ Тест на парсинг поля type """

        obj = Phone({"type": "phone"})
        self.assertEqual(obj.context, {"type": "phone"})
        self.assertEqual(obj.type, "phone")

        obj = Phone({"type": "fax"})
        self.assertEqual(obj.context, {"type": "fax"})
        self.assertEqual(obj.type, "fax")

    def test_destruct_formatted(self):
        """ Тест на парсинг поля formatted """

        obj = Phone({"formatted": "+7 992 92 92"})
        self.assertEqual(obj.context, {"formatted": "+7 992 92 92"})
        self.assertEqual(obj.formatted, "+7 992 92 92")

        obj = Phone({"formatted": "+7 91 123 92"})
        self.assertEqual(obj.context, {"formatted": "+7 91 123 92"})
        self.assertEqual(obj.formatted, "+7 91 123 92")

    def test_destruct(self):
        """ Тест на парсинг полного контекста """

        obj = Phone({"type": "phone", "formatted": "+7 91 443 92"})
        self.assertEqual(obj.context, {"type": "phone", "formatted": "+7 91 443 92"})
        self.assertEqual(obj.type, "phone")
        self.assertEqual(obj.formatted, "+7 91 443 92")

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = Phone({})
        self.assertEqual(obj.context, {})
        self.assertEqual(obj.type, None)

        with self.assertRaises(MissingRequiredProperty) as formatted_context:
            obj_formatted = obj.formatted

        formatted_context.exception("+7 91 123 92")
        self.assertEqual(obj.formatted, "+7 91 123 92")

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = Phone({})
        self.assertEqual(obj.context, {})

        obj.type = "phone"
        self.assertEqual(obj.type, "phone")

        obj.formatted = "+12 12312 123123"
        self.assertEqual(obj.formatted, "+12 12312 123123")

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = Phone({})
        self.assertEqual(obj.context, {})

        obj.type = "point"
        self.assertEqual(obj.type, "point")

        obj.formatted = "+81293 12312"
        self.assertEqual(obj.formatted, "+81293 12312")

        del obj.type
        self.assertEqual(obj.type, "")

        del obj.formatted
        with self.assertRaises(MissingRequiredProperty) as formatted_context:
            obj_formatted = obj.formatted


if __name__ == '__main__':
    unittest.main()