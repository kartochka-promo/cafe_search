
from ..avability import Availability
import unittest


class TestAvailability(unittest.TestCase):
    """ Класс для тестирования класса Availability """

    def test_init(self):
        """ Тест на инициализацию класса Geometry """
        obj = Availability({})
        self.assertEqual(obj.context, {})

        obj = Availability(None)
        self.assertEqual(obj.context, None)

        obj = Availability(123)
        self.assertEqual(obj.context, 123)

        obj = Availability([])
        self.assertEqual(obj.context, [])

        obj = Availability(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct_intervals(self):
        """ Тест на парсинг поля Intervals """

        obj = Availability({'Intervals': [{'from': '09:00:00', 'to': '13:00:00'},
                                          {'from': '14:00:00', 'to': '18:00:00'}]})

        self.assertEqual(obj.context, {'Intervals': [{'from': '09:00:00', 'to': '13:00:00'},
                                                     {'from': '14:00:00', 'to': '18:00:00'}]})

        self.assertEqual(obj.intervals, [['09:00:00', '13:00:00'],
                                         ['14:00:00', '18:00:00']])

    def test_destruct_twenty_four_hours(self):
        """ Тест на парсинг поля TwentyFourHours """

        obj = Availability({'Intervals': [{'from': '09:00:00', 'to': '13:00:00'},
                                          {'from': '14:00:00', 'to': '18:00:00'}]})

        self.assertEqual(obj.context, {'Intervals': [{'from': '09:00:00', 'to': '13:00:00'},
                                                     {'from': '14:00:00', 'to': '18:00:00'}]})

        self.assertEqual(obj.intervals, [['09:00:00', '13:00:00'],
                                         ['14:00:00', '18:00:00']])

        self.assertEqual(obj.twenty_four_hours, None)

        obj = Availability({'TwentyFourHours': True, 'Everyday': True})
        self.assertEqual(obj.context, {'TwentyFourHours': True, 'Everyday': True})
        self.assertEqual(obj.twenty_four_hours, True)

    def test_destruct_days(self):
        """ Тест на парсинг поля days """

        obj = Availability({'Monday': True, 'Tuesday': True,
                            'Wednesday': True, 'Thursday': True, 'Friday': True})

        self.assertEqual(obj.context, {'Monday': True, 'Tuesday': True,
                                       'Wednesday': True, 'Thursday': True, 'Friday': True})

        self.assertEqual(obj.days, {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'})

        obj = Availability({'Everyday': True})
        self.assertEqual(obj.context, {'Everyday': True})
        self.assertEqual(obj.days, {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Saturday", "Sunday"})

        obj = Availability({'Weekend': True})
        self.assertEqual(obj.context, {'Weekend': True})
        self.assertEqual(obj.days, {"Saturday", "Sunday"})

        obj = Availability({'Weekdays': True})
        self.assertEqual(obj.context, {'Weekdays': True})
        self.assertEqual(obj.days, {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'})

        obj = Availability({'Weekend': True, 'Weekdays': True})
        self.assertEqual(obj.context, {'Weekend': True, 'Weekdays': True})
        self.assertEqual(obj.days, {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Saturday", "Sunday"})

        obj = Availability({'Weekend': True, 'Monday': True})
        self.assertEqual(obj.context, {'Weekend': True, 'Monday': True})
        self.assertEqual(obj.days, {"Saturday", "Sunday", "Monday"})

        obj = Availability({'Weekend': True, 'Sunday': True})
        self.assertEqual(obj.context, {'Weekend': True, 'Sunday': True})
        self.assertEqual(obj.days, {"Saturday", "Sunday"})

    def test_destruct(self):
        """ Тест на парсинг полного контекста """

        obj = Availability({'Intervals': [
            {'from': '09:00:00', 'to': '13:00:00'},
            {'from': '14:00:00', 'to': '18:00:00'}
        ], 'Monday': True, 'Tuesday': True,
            'Wednesday': True, 'Thursday': True, 'Friday': True})

        self.assertEqual(obj.context, {'Intervals': [
            {'from': '09:00:00', 'to': '13:00:00'},
            {'from': '14:00:00', 'to': '18:00:00'}
        ], 'Monday': True, 'Tuesday': True,
            'Wednesday': True, 'Thursday': True, 'Friday': True})

        self.assertEqual(obj.intervals, [['09:00:00', '13:00:00'], ['14:00:00', '18:00:00']])
        self.assertEqual(obj.twenty_four_hours, None)
        self.assertEqual(obj.days, {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'})

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = Availability({})
        self.assertEqual(obj.context, {})
        self.assertEqual(obj.intervals, [])
        self.assertEqual(obj.twenty_four_hours, None)
        self.assertEqual(obj.days, set())

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = Availability({})
        self.assertEqual(obj.context, {})

        obj.intervals = [['1', '2'], ['3', '4']]
        self.assertEqual(obj.intervals, [['1', '2'], ['3', '4']])

        obj.twenty_four_hours = False
        self.assertEqual(obj.twenty_four_hours, False)

        obj.days = {'Monday', 'Friday'}
        self.assertEqual(obj.days, {'Monday', 'Friday'})

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = Availability({})
        self.assertEqual(obj.context, {})

        obj.intervals = [['1', '2'], ['3', '4']]
        self.assertEqual(obj.intervals, [['1', '2'], ['3', '4']])
        del obj.intervals
        self.assertEqual(obj.intervals, [])

        obj.twenty_four_hours = False
        self.assertEqual(obj.twenty_four_hours, False)
        del obj.twenty_four_hours
        self.assertEqual(obj.twenty_four_hours, None)

        obj.days = {'Monday', 'Friday'}
        self.assertEqual(obj.days, {'Monday', 'Friday'})
        del obj.days
        self.assertEqual(obj.days, set())


if __name__ == '__main__':
    unittest.main()