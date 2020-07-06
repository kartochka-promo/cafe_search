
from ...base.base import DestructObject
from ...exceptions.exceptions import MissingRequiredProperty

import numpy as np
from typing import Dict
from typing import List


class SearchRequest(DestructObject):
    
    def __init__(self, context: Dict) -> None:
        self.__request: str | None = None
        self.__results: int | None = None
        self.__skip: int | None = None
        self.__bounded_by: List[np.array] = []
        super(SearchRequest, self).__init__(context)

    def _destruct(self) -> None:
        self.__destruct_simple_properties()
        self.__destruct_bound(self._context.get("boundedBy"))

    def __destruct_simple_properties(self) -> None:
        self.__request: str | None = self._context.get("request")
        self.__results: int | None = self._context.get("results")
        self.__skip: int | None = self._context.get("skip")

    def __destruct_bound(self, bounded_by : List[List[int]]) -> None:
        if bounded_by:
            self.__bounded_by = [np.array(point) for point in bounded_by]

    def get_request(self) -> str:
        if self.__request:
            return self.__request
        else:
            raise MissingRequiredProperty(self.set_request)

    def set_request(self, request) -> None:
        self.__request: str | None = request

    def del_request(self) -> None:
        self.__request: str | None = None

    def get_results(self) -> int | None:
        return self.__results

    def set_results(self, results: int | None):
        self.__results: int | None = results

    def del_results(self) -> None:
        self.__results: int | None = None

    def get_skip(self) -> int | None:
        return self.__skip

    def set_skip(self, skip) -> None:
        self.__skip: int | None = skip

    def del_skip(self) -> None:
        self.__skip: int | None = None

    def get_bounded_by(self) -> List[np.array]:
        return self.__bounded_by

    def set_bounded_by(self, bounded_by: List[List[int]]):
        self.__destruct_bound(bounded_by)

    def del_bounded_by(self) -> None:
        self.__bounded_by: List[np.array] = []

    request = property(get_request, set_request, del_request, doc="")
    results = property(get_results, set_results, del_results, doc="")
    skip = property(get_skip, set_skip, del_skip, doc="")
    bounded_by = property(get_bounded_by, set_bounded_by, del_bounded_by, doc="")
