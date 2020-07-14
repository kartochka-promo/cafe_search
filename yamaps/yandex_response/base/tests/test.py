
import unittest
from yamaps.yandex_response.base.base import DestructObject


class TestDestructObject(unittest.TestCase):
    """ Класс для тестирования класса DestructObject """

    def test_global(self):
        """ Тест класса DestructObject """
        obj = DestructObject({})
        self.assertEqual(obj.context, {})

        obj = DestructObject(None)
        self.assertEqual(obj.context, None)

        obj = DestructObject(123)
        self.assertEqual(obj.context, 123)

        obj = DestructObject([])
        self.assertEqual(obj.context, [])

        obj = DestructObject(123.123)
        self.assertEqual(obj.context, 123.123)


if __name__ == '__main__':
    unittest.main()
