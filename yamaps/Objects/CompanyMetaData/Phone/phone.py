
from typing import Dict
from Objects.Base.base import DestructObject
from Objects.Exceptions.exceptions import MissingRequiredProperty


class Phone(DestructObject):

    def __init__(self, context: Dict) -> None:
        self.__type: str = ""
        self.__formatted: str | None = None
        super(Phone, self).__init__(context)

    def _destruct(self) -> None:
        self.__type: str = self._context.get("type")
        self.__formatted: str | None = self._context.get("formatted")

    def get_type(self) -> str:
        return self.__type

    def set_type(self, type: str) -> None:
        self.__type: str = type

    def del_type(self) -> None:
        self.__type: str = ""

    def get_formatted(self) -> str:
        if self.__formatted:
            return self.__formatted
        else:
            raise MissingRequiredProperty(self.set_formatted)

    def set_formatted(self, formatted: str | None):
        self.__formatted: str | None = formatted

    def del_formatted(self):
        self.__formatted: str | None = None

    type = property(get_type, set_type, del_type, doc="")
    formatted = property(get_formatted, set_formatted, del_formatted, doc="")
