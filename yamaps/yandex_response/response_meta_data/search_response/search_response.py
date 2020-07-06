
from ...base.base import DestructObject
from ...exceptions.exceptions import MissingRequiredProperty

from typing import List
from typing import Dict
import numpy as np


class SearchResponse(DestructObject):

    def __init__(self, context: Dict) -> None:
        self.__found: int | None = None
        self.__display: str | None = None
        self.__bounded_by: List[np.array] = []
        super(SearchResponse, self).__init__(context)

    def _destruct(self) -> None:
        self.__destruct_simple_properties()
        self.__destruct_bound(self._context.get("boundedBy"))

    def __destruct_simple_properties(self) -> None:
        self.__found: int | None = self._context.get("found")
        self.__display: str | None = self._context.get("display")

    def __destruct_bound(self, bounded_by : List[List[int]]) -> None:
        if bounded_by:
            self.__bounded_by = [np.array(point) for point in bounded_by]

    def get_found(self) -> int | None:
        if self.__found:
            return self.__found
        else:
            raise MissingRequiredProperty(self.set_found)

    def set_found(self, found: int | None) -> None:
        self.__found: int | None = found

    def del_found(self) -> None:
        self.__found: int | None = None

    def get_bounded_by(self) -> List[np.array]:
        return self.__bounded_by

    def set_bounded_by(self, bounded_by: List[List[int]]):
        self.__destruct_bound(bounded_by)

    def del_bounded_by(self) -> None:
        self.__bounded_by: List[np.array] = []

    def get_display(self) -> str | None:
        return self.__display

    def set_display(self, display: str | None) -> None:
        self.__display: str | None = display

    def del_display(self) -> None:
        self.__display: str | None = None

    found = property(get_found, set_found, del_found, doc="")
    bounded_by = property(get_bounded_by, set_bounded_by, del_bounded_by, doc="")
    display = property(get_display, set_display, del_display, doc="")




