import unittest
from ..search_request import SearchRequest
from ....exceptions.exceptions import MissingRequiredProperty


class TestSearchRequest(unittest.TestCase):
    """ Класс для тестирования класса SearchRequest """

    def test_init(self):
        """ Тест на инициализацию класса SearchRequest """
        obj = SearchRequest({})
        self.assertEqual(obj.context, {})

        obj = SearchRequest(None)
        self.assertEqual(obj.context, None)

        obj = SearchRequest(123)
        self.assertEqual(obj.context, 123)

        obj = SearchRequest([])
        self.assertEqual(obj.context, [])

        obj = SearchRequest(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct_simple_properties(self):
        """ Тест на парсинг простых(не вложенных) свойств """

        obj = SearchRequest({'request': 'Военкомат', 'skip': 0, 'results': 10})
        self.assertEqual(obj.context, {'request': 'Военкомат', 'skip': 0, 'results': 10})

        self.assertEqual(obj.request, 'Военкомат')
        self.assertEqual(obj.skip, 0)
        self.assertEqual(obj.results, 10)

    def test_destruct_bound(self):
        """ Тест на парсинг свойства boundedBy """

        obj = SearchRequest({'boundedBy': [[37.048427, 55.43644866], [38.175903, 56.04690174]]})
        self.assertEqual(obj.context, {'boundedBy': [[37.048427, 55.43644866], [38.175903, 56.04690174]]})

        self.assertEqual(obj.bounded_by[0][0], 37.048427)
        self.assertEqual(obj.bounded_by[0][1], 55.43644866)
        self.assertEqual(obj.bounded_by[1][0], 38.175903)
        self.assertEqual(obj.bounded_by[1][1], 56.04690174)

    def test_destruct(self):
        """ Тест на парсинг полного контекста """

        obj = SearchRequest({'request': 'Военкомат',
                             'skip': 0, 'results': 10,
                             'boundedBy': [[37.048427, 55.43644866], [38.175903, 56.04690174]]})

        self.assertEqual(obj.context, {'request': 'Военкомат',
                                       'skip': 0, 'results': 10,
                                       'boundedBy': [[37.048427, 55.43644866], [38.175903, 56.04690174]]})

        self.assertEqual(obj.request, 'Военкомат')
        self.assertEqual(obj.skip, 0)
        self.assertEqual(obj.results, 10)

        self.assertEqual(obj.bounded_by[0][0], 37.048427)
        self.assertEqual(obj.bounded_by[0][1], 55.43644866)
        self.assertEqual(obj.bounded_by[1][0], 38.175903)
        self.assertEqual(obj.bounded_by[1][1], 56.04690174)

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = SearchRequest({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as request_context:
            obj_request = obj.request

        request_context.exception("sample request")
        self.assertEqual(obj.request, "sample request")

        self.assertEqual(obj.skip, None)
        self.assertEqual(obj.results, None)
        self.assertEqual(obj.bounded_by, [])

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = SearchRequest({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as request_context:
            obj_request = obj.request

        self.assertEqual(obj.skip, None)
        self.assertEqual(obj.results, None)
        self.assertEqual(obj.bounded_by, [])

        obj.request = "123"
        self.assertEqual(obj.request, "123")

        obj.skip = 50
        self.assertEqual(obj.skip, 50)

        obj.results = 100
        self.assertEqual(obj.results, 100)

        obj.bounded_by = [[1, 2], [3, 4]]
        self.assertEqual(obj.bounded_by[0][0], 1)
        self.assertEqual(obj.bounded_by[0][1], 2)
        self.assertEqual(obj.bounded_by[1][0], 3)
        self.assertEqual(obj.bounded_by[1][1], 4)

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = SearchRequest({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as request_context:
            obj_request = obj.request

        self.assertEqual(obj.skip, None)
        self.assertEqual(obj.results, None)
        self.assertEqual(obj.bounded_by, [])

        obj.request = "123"
        self.assertEqual(obj.request, "123")

        obj.skip = 50
        self.assertEqual(obj.skip, 50)

        obj.results = 100
        self.assertEqual(obj.results, 100)

        obj.bounded_by = [[1, 2], [3, 4]]
        self.assertEqual(obj.bounded_by[0][0], 1)
        self.assertEqual(obj.bounded_by[0][1], 2)
        self.assertEqual(obj.bounded_by[1][0], 3)
        self.assertEqual(obj.bounded_by[1][1], 4)

        del obj.request
        with self.assertRaises(MissingRequiredProperty) as request_context:
            obj_request = obj.request

        del obj.results
        self.assertEqual(obj.results, None)

        del obj.skip
        self.assertEqual(obj.skip, None)

        del obj.bounded_by
        self.assertEqual(obj.bounded_by, [])


if __name__ == '__main__':
    unittest.main()
