
import unittest

from yamaps.yandex_response.response_meta_data.search_response.search_response import SearchResponse
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty


class TestSearchResponse(unittest.TestCase):
    """ Класс для тестирования класса SearchResponse """

    def test_init(self):
        """ Тест на инициализацию класса SearchResponse """
        obj = SearchResponse({})
        self.assertEqual(obj.context, {})

        obj = SearchResponse(None)
        self.assertEqual(obj.context, None)

        obj = SearchResponse(123)
        self.assertEqual(obj.context, 123)

        obj = SearchResponse([])
        self.assertEqual(obj.context, [])

        obj = SearchResponse(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct_simple_properties(self):
        """ Тест на парсинг простых(не вложенных) свойств """

        obj = SearchResponse({'found': 90, 'display': 'multiple'})
        self.assertEqual(obj.context, {'found': 90, 'display': 'multiple'})
        self.assertEqual(obj.found, 90)
        self.assertEqual(obj.display, 'multiple')

    def test_destruct_bound(self):
        """ Тест на парсинг свойства boundedBy """

        obj = SearchResponse({"boundedBy": [
            [
                37.76257841,
                55.71649343
            ],
            [
                37.76644117,
                55.72008348
            ]
        ]})

        self.assertEqual(obj.bounded_by[0][0], 37.76257841)
        self.assertEqual(obj.bounded_by[0][1], 55.71649343)
        self.assertEqual(obj.bounded_by[1][0], 37.76644117)
        self.assertEqual(obj.bounded_by[1][1], 55.72008348)

    def test_destruct(self):
        """ Тест на парсинг полного контекста """

        obj = SearchResponse({
            "found": 36,
            "boundedBy": [
                [
                    37.76257841,
                    55.71649343
                ],
                [
                    37.76644117,
                    55.72008348
                ]
            ],
            "display": "multiple"
        })

        self.assertEqual(obj.context, {
            "found": 36,
            "boundedBy": [
                [
                    37.76257841,
                    55.71649343
                ],
                [
                    37.76644117,
                    55.72008348
                ]
            ],
            "display": "multiple"
        })

        self.assertEqual(obj.found, 36)
        self.assertEqual(obj.display, "multiple")
        self.assertEqual(obj.bounded_by[0][0], 37.76257841)
        self.assertEqual(obj.bounded_by[0][1], 55.71649343)
        self.assertEqual(obj.bounded_by[1][0], 37.76644117)
        self.assertEqual(obj.bounded_by[1][1], 55.72008348)

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = SearchResponse({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as found_context:
            obj_found = obj.found

        found_context.exception(123)
        self.assertEqual(obj.found, 123)

        self.assertEqual(obj.display, None)
        self.assertEqual(obj.bounded_by, [])

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = SearchResponse({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as found_context:
            obj_found = obj.found

        found_context.exception(123)
        self.assertEqual(obj.found, 123)

        self.assertEqual(obj.display, None)
        obj.display = "sample"
        self.assertEqual(obj.display, "sample")

        self.assertEqual(obj.bounded_by, [])
        obj.bounded_by = [[1, 2], [3, 4]]
        self.assertEqual(obj.bounded_by[0][0], 1)
        self.assertEqual(obj.bounded_by[0][1], 2)
        self.assertEqual(obj.bounded_by[1][0], 3)
        self.assertEqual(obj.bounded_by[1][1], 4)

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = SearchResponse({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as found_context:
            obj_found = obj.found

        found_context.exception(123)
        self.assertEqual(obj.found, 123)

        self.assertEqual(obj.display, None)
        obj.display = "sample"
        self.assertEqual(obj.display, "sample")

        self.assertEqual(obj.bounded_by, [])
        obj.bounded_by = [[1, 2], [3, 4]]
        self.assertEqual(obj.bounded_by[0][0], 1)
        self.assertEqual(obj.bounded_by[0][1], 2)
        self.assertEqual(obj.bounded_by[1][0], 3)
        self.assertEqual(obj.bounded_by[1][1], 4)

        del obj.found
        with self.assertRaises(MissingRequiredProperty) as found_context:
            obj_found = obj.found

        del obj.display
        self.assertEqual(obj.display, None)

        del obj.bounded_by
        self.assertEqual(obj.bounded_by, [])


if __name__ == '__main__':
    unittest.main()