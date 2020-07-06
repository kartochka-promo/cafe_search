
from objects.base.base import DestructObject
from objects.exceptions.exceptions import MissingRequiredProperty
from ..response_meta_data.search_request.search_request import SearchRequest
from ..response_meta_data.search_response.search_response import SearchResponse


class ResponseMetaData(DestructObject):
    
    def __init__(self, context: dict) -> None:
        self.__search_request: SearchRequest | None = None
        self.__search_response: SearchResponse | None = None
        super(ResponseMetaData, self).__init__(context)

    def _destruct(self) -> None:
        self.__destruct_search_request(self._context.get("SearchRequest"))
        self.__destruct_search_response(self._context.get("SearchResponse"))

    def __destruct_search_request(self, search_request_context) -> None:
        if search_request_context:
            self.__search_request: SearchRequest | None = SearchRequest(search_request_context)

    def __destruct_search_response(self, search_response_context) -> None:
        if search_response_context:
            self.__search_response: SearchResponse | None = SearchResponse(search_response_context)

    def get_search_response(self) -> SearchResponse:
        if self.__search_response:
            return self.__search_response
        else:
            raise MissingRequiredProperty(self.set_search_response)

    def set_search_response(self, search_response_context: dict) -> None:
        self.__destruct_search_response(search_response_context)

    def del_search_response(self) -> None:
        self.__search_response: SearchResponse | None = None

    def get_search_request(self) -> SearchRequest:
        if self.__search_request:
            return self.__search_request
        else:
            raise MissingRequiredProperty(self.set_search_request)

    def set_search_request(self, search_request_context: dict) -> None:
        self.__destruct_search_request(search_request_context)

    def del_search_request(self) -> None:
        self.__search_request: SearchRequest | None = None

    search_response = property(get_search_response, set_search_response, del_search_response, doc="")
    search_request = property(get_search_request, set_search_request, del_search_request, doc="")
