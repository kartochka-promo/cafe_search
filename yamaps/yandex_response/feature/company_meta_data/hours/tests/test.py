
import unittest
from ..hours import Hours
from ..avability.avability import Availability
from .....exceptions.exceptions import MissingRequiredProperty


class TestHours(unittest.TestCase):
    """ Класс для тестирования класса Availability """

    def test_init(self):
        """ Тест на инициализацию класса Geometry """
        obj = Hours({})
        self.assertEqual(obj.context, {})

        obj = Hours(None)
        self.assertEqual(obj.context, None)

        obj = Hours(123)
        self.assertEqual(obj.context, 123)

        obj = Hours([])
        self.assertEqual(obj.context, [])

        obj = Hours(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct_text(self):
        """ Тест на парсинг поля text """

        obj = Hours({'text': 'sample text'})
        self.assertEqual(obj.context, {'text': 'sample text'})
        self.assertEqual(obj.text, 'sample text')

    def test_destruct_availabilities(self):
        """ Тест на парсинг поля Availabilities """

        obj = Hours({'Availabilities': [{'Intervals': [
            {'from': '09:00:00', 'to': '13:00:00'},
            {'from': '14:00:00', 'to': '18:00:00'}],
            'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True}]})

        self.assertEqual(obj.context, {'Availabilities': [{'Intervals': [
            {'from': '09:00:00', 'to': '13:00:00'},
            {'from': '14:00:00', 'to': '18:00:00'}],
            'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True}]})

        self.assertIs(type(obj.availabilities), list)
        self.assertEqual(len(obj.availabilities), 1)

        obj = Hours({'Availabilities': [None, None]})
        self.assertEqual(obj.context, {'Availabilities': [None, None]})
        self.assertIs(type(obj.availabilities), list)
        self.assertEqual(len(obj.availabilities), 2)

    def test_destruct(self):
        """ Тест на парсинг полного контекста """

        obj = Hours({'text': 'пн-пт 9:00–18:00, перерыв 13:00–14:00',
                     'Availabilities': [
                         {'Intervals': [
                             {'from': '09:00:00', 'to': '13:00:00'},
                             {'from': '14:00:00', 'to': '18:00:00'}
                         ],
                             'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True
                         }
                     ]})

        self.assertEqual(obj.context, {'text': 'пн-пт 9:00–18:00, перерыв 13:00–14:00',
                                       'Availabilities': [
                                           {'Intervals':[
                                               {'from': '09:00:00', 'to': '13:00:00'},
                                               {'from': '14:00:00', 'to': '18:00:00'}
                                           ],
                                               'Monday': True, 'Tuesday': True,
                                               'Wednesday': True, 'Thursday': True, 'Friday': True
                                           }]})

        self.assertEqual(obj.text, 'пн-пт 9:00–18:00, перерыв 13:00–14:00')
        self.assertIs(type(obj.availabilities), list)
        self.assertEqual(len(obj.availabilities), 1)

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = Hours({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as text_context:
            obj_text = obj.text

        text_context.exception("tests context")
        self.assertEqual(obj.text, "tests context")
        self.assertEqual(obj.availabilities, [])

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = Hours({})
        self.assertEqual(obj.context, {})

        obj.text = "some text"
        self.assertEqual(obj.text, "some text")

        obj.availabilities = [{'Intervals': [
            {'from': '09:00:00', 'to': '13:00:00'},
            {'from': '14:00:00', 'to': '18:00:00'}
        ],
            'Monday': True, 'Tuesday': True, 'Wednesday': True,
            'Thursday': True, 'Friday': True
        }]

        self.assertIs(type(obj.availabilities), list)
        self.assertEqual(len(obj.availabilities), 1)
        self.assertEqual(obj.availabilities[0].days,
                         {'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday'})

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = Hours({})
        self.assertEqual(obj.context, {})

        obj.text = "some text"
        self.assertEqual(obj.text, "some text")

        obj.availabilities = [{'Intervals': [
            {'from': '09:00:00', 'to': '13:00:00'},
            {'from': '14:00:00', 'to': '18:00:00'}
        ],
            'Monday': True, 'Tuesday': True, 'Wednesday': True,
            'Thursday': True, 'Friday': True
        }]

        self.assertIs(type(obj.availabilities), list)
        self.assertEqual(len(obj.availabilities), 1)
        self.assertEqual(obj.availabilities[0].days,
                         {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'})

        del obj.text
        with self.assertRaises(MissingRequiredProperty) as text_context:
            obj_text = obj.text

        del obj.availabilities
        self.assertEqual(obj.availabilities, [])


if __name__ == '__main__':
    unittest.main()