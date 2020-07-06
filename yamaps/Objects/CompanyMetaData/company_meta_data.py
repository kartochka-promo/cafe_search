
from typing import Dict
from typing import List

from Objects.Base.base import DestructObject
from Objects.Exceptions.exceptions import MissingRequiredProperty

from Objects.CompanyMetaData.Phone.phone import Phone
from Objects.CompanyMetaData.Category.category import Category
from Objects.CompanyMetaData.Hours.hours import Hours


class CompanyMetaData(DestructObject):

    def __init__(self, context: Dict) -> None:
        self.__id: str | None = None
        self.__name: str | None = None
        self.__address: str = ""
        self.__url: str = ""
        self.__categories: List[Category] = []
        self.__phones: List[Phone] = []
        self.__hours: Hours | None = None
        super(CompanyMetaData, self).__init__(context)

    def _destruct(self) -> None:
        self.__destruct_simple_properties()
        self.__destruct_categories(self._context.get("Categories"))
        self.__destruct_phones(self._context.get("Phones"))
        self.__destruct_hours(self._context.get("hours"))

    def __destruct_simple_properties(self) -> None:
        self.__id: str | None = self._context.get("id")
        self.__name: str | None = self._context.get("name")
        self.__address: str = self._context.get("address")
        self.__url: str = self._context.get("url")

    def __destruct_categories(self, categories_context) -> None:
        if categories_context:
            self.__categories: List[Category] = [Category(category) for category in categories_context]

    def __destruct_phones(self, phones_context):
        if phones_context:
            self.__phones: List[Phone] = [Phone(contact) for contact in phones_context]

    def __destruct_hours(self, hours_context):
        if hours_context:
            self.__hours: Hours = Hours(hours_context)

    def get_id(self) -> str:
        if self.__id:
            return self.__id
        else:
            raise MissingRequiredProperty(self.set_id)

    def set_id(self, id: str | None) -> None:
        self.__id: str | None = id

    def del_id(self) -> None:
        self.__id: str | None = None

    def get_name(self) -> str:
        if self.__name:
            return self.__name
        else:
            raise MissingRequiredProperty(self.set_name)

    def set_name(self, name) -> None:
        self.__name: str | None = name

    def del_name(self) -> None:
        self.__name: str | None = None

    def get_address(self) -> str | None:
        return self.__address

    def set_address(self, address: str) -> None:
        self.__address: str = address

    def del_address(self) -> None:
        self.__address: str = ""

    def get_url(self) -> str:
        return self.__url

    def set_url(self, url: str) -> None:
        self.__url: str = url

    def del_url(self) -> None:
        self.__url: str = ""

    def get_categories(self) -> List[Category]:
        return self.__categories

    def set_categories(self, categories: List[Dict]):
        self.__destruct_categories(categories)

    def del_categories(self) -> None:
        self.__categories: List[Category] = []

    def get_phones(self) -> List[Phone]:
        return self.__phones

    def set_phones(self, phones: List[Dict]):
        self.__destruct_phones(phones)

    def del_phones(self) -> None:
        self.__phones: List[Phone] = []

    def get_hours(self) -> Hours | None:
        return self.__hours

    def set_hours(self, hours: List[Dict]) -> None:
        self.__destruct_hours(hours)

    def del_hours(self):
        self.__hours: Hours | None = None
