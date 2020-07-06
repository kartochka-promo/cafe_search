
from typing import Dict
from Objects.Base.base import DestructObject
from Objects.Exceptions.exceptions import MissingRequiredProperty


class Category(DestructObject):

    def __init__(self, context: Dict) -> None:
        self.__cls: str = ""
        self.__name: str | None = None
        super(Category, self).__init__(context)

    def _destruct(self) -> None:
        self.__cls: str = self._context.get("class")
        self.__name: str | None = self._context.get("name")

    def get_class(self) -> str:
        return self.__cls

    def set_class(self, cls: str) -> None:
        self.__cls: str = cls

    def del_class(self) -> None:
        self.__cls: str = ""

    def get_name(self) -> str:
        if self.__name:
            return self.__name
        else:
            raise MissingRequiredProperty(self.set_name)

    def set_name(self, name: str | None) -> None:
        self.__name: str | None = name

    def del_name(self) -> None:
        self.__name: str | None = None

    cls = property(get_class, set_class, del_class, doc="")
    name = property(get_name, set_name, del_name, doc="")
