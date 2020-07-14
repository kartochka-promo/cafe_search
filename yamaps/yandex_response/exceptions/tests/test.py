
import unittest
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty


class TestMissingRequiredProperty(unittest.TestCase):
    """ Класс для тестирования класса MissingRequiredProperty """

    def test_global(self):
        """ Тест класса MissingRequiredProperty """

        self.obj = None

        def setter(value):
            self.obj = value

        with self.assertRaises(MissingRequiredProperty) as context:
            raise MissingRequiredProperty(setter)

        context.exception(12)
        self.assertEqual(self.obj, 12)


if __name__ == '__main__':
    unittest.main()
