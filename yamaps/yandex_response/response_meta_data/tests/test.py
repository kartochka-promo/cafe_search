import unittest
from ..response_meta_data import ResponseMetaData
from ..search_request.search_request import SearchRequest
from ..search_response.search_response import SearchResponse
from ...exceptions.exceptions import MissingRequiredProperty


class TestResponseMetaData(unittest.TestCase):
    """ Класс для тестирования класса ResponseMetaData """

    def test_init(self):
        """ Тест на инициализацию класса ResponseMetaData """
        obj = ResponseMetaData({})
        self.assertEqual(obj.context, {})

        obj = ResponseMetaData(None)
        self.assertEqual(obj.context, None)

        obj = ResponseMetaData(123)
        self.assertEqual(obj.context, 123)

        obj = ResponseMetaData([])
        self.assertEqual(obj.context, [])

        obj = ResponseMetaData(123.123)
        self.assertEqual(obj.context, 123.123)

    def test_destruct_search_request(self):
        """ Тест на парсинг свойства SearchRequest """

        obj = ResponseMetaData({ 'SearchRequest': {
            'request': 'Военкомат',
            'skip': 0,
            'results': 10,
            'boundedBy': [[37.048427, 55.43644866], [38.175903, 56.04690174]]}
        })

        self.assertEqual(obj.context, {
            'SearchRequest': {
                'request': 'Военкомат',
                'skip': 0,
                'results': 10,
                'boundedBy': [[37.048427, 55.43644866], [38.175903, 56.04690174]]
            }
        })

        self.assertIs(type(obj.search_request), SearchRequest)

    def test_destruct_search_response(self):
        """ Тест на парсинг свойства SearchResponse """

        obj = ResponseMetaData({'SearchResponse': {'found': 90, 'display': 'multiple'}})
        self.assertEqual(obj.context, {'SearchResponse': {'found': 90, 'display': 'multiple'}})
        self.assertIs(type(obj.search_response), SearchResponse)

    def test_destruct(self):
        """ Тест на парсинг полного контекста """

        obj = ResponseMetaData({'SearchResponse': {
            'found': 90,
            'display': 'multiple'
        }, 'SearchRequest': {
            'request': 'Военкомат',
            'skip': 0,
            'results': 10,
            'boundedBy': [[37.048427, 55.43644866], [38.175903, 56.04690174]]
        }})

        self.assertEqual(obj.context, {'SearchResponse': {
            'found': 90,
            'display': 'multiple'
        }, 'SearchRequest': {
            'request': 'Военкомат',
            'skip': 0,
            'results': 10,
            'boundedBy': [[37.048427, 55.43644866], [38.175903, 56.04690174]]
        }})

        self.assertIs(type(obj.search_request), SearchRequest)
        self.assertIs(type(obj.search_response), SearchResponse)

    def test_getters(self):
        """ Тест, проверяющий работу getters """

        obj = ResponseMetaData({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as search_request_context:
            obj_search_request = obj.search_request

        with self.assertRaises(MissingRequiredProperty) as search_response_context:
            obj_search_response = obj.search_response

    def test_setters(self):
        """ Тест, проверяющий работу setters """

        obj = ResponseMetaData({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as search_request_context:
            obj_search_request = obj.search_request

        search_request_context.exception({})
        self.assertIs(type(obj.search_request), SearchRequest)

        with self.assertRaises(MissingRequiredProperty) as search_response_context:
            obj_search_response = obj.search_response

        search_response_context.exception({})
        self.assertIs(type(obj.search_response), SearchResponse)

    def test_deleters(self):
        """ Тест, проверяющий работу deleters """

        obj = ResponseMetaData({})
        self.assertEqual(obj.context, {})

        with self.assertRaises(MissingRequiredProperty) as search_request_context:
            obj_search_request = obj.search_request

        search_request_context.exception({})
        self.assertIs(type(obj.search_request), SearchRequest)

        with self.assertRaises(MissingRequiredProperty) as search_response_context:
            obj_search_response = obj.search_response

        search_response_context.exception({})
        self.assertIs(type(obj.search_response), SearchResponse)

        del obj.search_request
        with self.assertRaises(MissingRequiredProperty) as search_request_context:
            obj_search_request = obj.search_request

        del obj.search_response
        with self.assertRaises(MissingRequiredProperty) as search_response_context:
            obj_search_response = obj.search_response


if __name__ == '__main__':
    unittest.main()
