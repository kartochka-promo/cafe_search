
from typing import Dict
from ..base.base import DestructObject
from ..exceptions.exceptions import MissingRequiredProperty
from ..response_meta_data.search_request.search_request import SearchRequest
from ..response_meta_data.search_response.search_response import SearchResponse


class ResponseMetaData(DestructObject):
    """
    Класс, описывающий метаданные, описывающие запрос и ответ.
    Конструируется из полученного объекта при запросе поиска организаций
    Обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса ResponseMetaData

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__search_request: SearchRequest | None = None
        self.__search_response: SearchResponse | None = None
        super(ResponseMetaData, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(self._context) is dict:
            self.__destruct_search_request(self._context.get("SearchRequest"))
            self.__destruct_search_response(self._context.get("SearchResponse"))

    def __destruct_search_request(self, search_request_context) -> None:
        """
        Метод, котрый разбирает контекст
        search_request, на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(search_request_context) is dict:
            self.__search_request: SearchRequest | None = SearchRequest(search_request_context)

    def __destruct_search_response(self, search_response_context) -> None:
        """
        Метод, котрый разбирает контекст
        search_response, на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(search_response_context) is dict:
            self.__search_response: SearchResponse | None = SearchResponse(search_response_context)

    def _get_search_response(self) -> type(SearchResponse):
        """
        Getter поля search_response
        (Метаданные, описывающие ответ. Обязательное поле.)

        :rtype: SearchResponse Метаданные, описывающие ответ. Обязательное поле.
        :return: возвращает значение поля search_response
        """

        if self.__search_response:
            return self.__search_response
        else:
            raise MissingRequiredProperty(self._set_search_response)

    def _set_search_response(self, search_response_context: Dict) -> None:
        """
        Setter поля search_response
        (Метаданные, описывающие ответ. Обязательное поле.)

        :type search_response_context: Dict
        :param search_response_context: Метаданные, описывающие ответ. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_search_response(search_response_context)

    def _del_search_response(self) -> None:
        """
        Deleter поля search_response
        (Метаданные, описывающие ответ. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__search_response: SearchResponse | None = None

    def _get_search_request(self) -> type(SearchRequest):
        """
        Getter поля search_request
        (Метаданные, описывающие запрос. Обязательное поле.)

        :rtype: SearchResponse Метаданные, описывающие запрос. Обязательное поле.
        :return: возвращает значение поля search_request
        """

        if self.__search_request:
            return self.__search_request
        else:
            raise MissingRequiredProperty(self._set_search_request)

    def _set_search_request(self, search_request_context: Dict) -> None:
        """
        Setter поля search_request
        (Метаданные, описывающие запрос. Обязательное поле.)

        :type search_request_context: Dict
        :param search_request_context: Метаданные, описывающие запрос. Обязательное поле..
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_search_request(search_request_context)

    def _del_search_request(self) -> None:
        """
        Deleter поля search_request
        (Метаданные, описывающие запрос. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__search_request: SearchRequest | None = None

    search_response = property(_get_search_response, _set_search_response, _del_search_response,
                               doc="Метаданные, описывающие ответ. Обязательное поле.")

    search_request = property(_get_search_request, _set_search_request, _del_search_request,
                              doc="Метаданные, описывающие запрос. Обязательное поле.")
