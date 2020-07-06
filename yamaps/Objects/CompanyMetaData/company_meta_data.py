
from typing import Dict
from typing import List

from Objects.Base.base import DestructObject
from Objects.Exceptions.exceptions import MissingRequiredProperty

from Objects.CompanyMetaData.Phone.phone import Phone
from Objects.CompanyMetaData.Category.category import Category
from Objects.CompanyMetaData.Hours.hours import Hours


class CompanyMetaData(DestructObject):
    """
    Класс, описывающий сведения об отдельной организации:
    адрес, контактную информацию, режим работы, вид деятельности и др.
    Конструируется из полученного объекта YandexMapsApi
    Не обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса CompanyMetaData

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__id: str | None = None
        self.__name: str | None = None
        self.__address: str = ""
        self.__url: str = ""
        self.__categories: List[Category] = []
        self.__phones: List[Phone] = []
        self.__hours: Hours | None = None
        super(CompanyMetaData, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_simple_properties()
        self.__destruct_categories(self._context.get("Categories"))
        self.__destruct_phones(self._context.get("Phones"))
        self.__destruct_hours(self._context.get("hours"))

    def __destruct_simple_properties(self) -> None:
        """
        Метод, котрый разбирает (не составные) поля
        из контекста, переданного в конструктор.

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__id: str | None = self._context.get("id")
        self.__name: str | None = self._context.get("name")
        self.__address: str = self._context.get("address")
        self.__url: str = self._context.get("url")

    def __destruct_categories(self, categories_context) -> None:
        """
        Метод, котрый разбирает составное поле categories
        из контекста, переданного в конструктор.

        :rtype: None
        :return: Ничего не возвращает
        """

        if categories_context:
            self.__categories: List[Category] = [Category(category) for category in categories_context]

    def __destruct_phones(self, phones_context):
        """
        Метод, котрый разбирает составное поле phones
        из контекста, переданного в конструктор.

        :rtype: None
        :return: Ничего не возвращает
        """

        if phones_context:
            self.__phones: List[Phone] = [Phone(contact) for contact in phones_context]

    def __destruct_hours(self, hours_context):
        """
        Метод, котрый разбирает составное поле hours
        из контекста, переданного в конструктор.

        :rtype: None
        :return: Ничего не возвращает
        """

        if hours_context:
            self.__hours: Hours = Hours(hours_context)

    def get_id(self) -> str:
        """
        Getter поля id
        (Идентификатор организации. Обязательное поле.)

        :rtype: str Идентификатор организации. Обязательное поле.
        :return: возвращает значение поля id
        """

        if self.__id:
            return self.__id
        else:
            raise MissingRequiredProperty(self.set_id)

    def set_id(self, id: str | None) -> None:
        """
        Setter поля id
        (Идентификатор организации. Обязательное поле.)

        :type id: str
        :param id: Идентификатор организации. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__id: str | None = id

    def del_id(self) -> None:
        """
        Deleter поля id
        (Идентификатор организации. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__id: str | None = None

    def get_name(self) -> str:
        """
        Getter поля name
        (Название организации. Обязательное поле.)

        :rtype: str Название организации. Обязательное поле.
        :return: возвращает значение поля name
        """

        if self.__name:
            return self.__name
        else:
            raise MissingRequiredProperty(self.set_name)

    def set_name(self, name) -> None:
        """
        Setter поля name
        (Название организации. Обязательное поле.)

        :type name: str
        :param name: Название организации. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__name: str | None = name

    def del_name(self) -> None:
        """
        Deleter поля name
        (Название организации. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__name: str | None = None

    def get_address(self) -> str:
        """
        Getter поля address
        (Адрес организации. Не обязательное поле.)

        :rtype: str Адрес организации. Не обязательное поле.
        :return: возвращает значение поля address
        """

        return self.__address

    def set_address(self, address: str) -> None:
        """
        Setter поля address
        (Адрес организации. Не обязательное поле.)

        :type address: str
        :param address: Адрес организации. Не обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__address: str = address

    def del_address(self) -> None:
        """
        Deleter поля address
        (Адрес организации. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__address: str = ""

    def get_url(self) -> str:
        """
        Getter поля url
        (Ссылка на сайт организации. Не обязательное поле.)

        :rtype: str Ссылка на сайт организации. Не обязательное поле.
        :return: возвращает значение поля url
        """

        return self.__url

    def set_url(self, url: str) -> None:
        """
        Setter поля url
        (Ссылка на сайт организации. Не обязательное поле.)

        :type url: str
        :param url: Ссылка на сайт организации. Не обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__url: str = url

    def del_url(self) -> None:
        """
        Deleter поля url
        (Ссылка на сайт организации. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__url: str = ""

    def get_categories(self) -> List[Category]:
        """
        Getter поля categories
        (Список категорий, в которые входит организация.)

        :rtype: List[Category] Список категорий, в которые входит организация.
        :return: возвращает значение поля categories
        """

        return self.__categories

    def set_categories(self, categories: List[Dict]):
        """
        Setter поля categories
        (Список категорий, в которые входит организация.)

        :type categories: List[Dict]
        :param categories: Список категорий, в которые входит организация.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_categories(categories)

    def del_categories(self) -> None:
        """
        Deleter поля categories
        (Список категорий, в которые входит организация.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__categories: List[Category] = []

    def get_phones(self) -> List[Phone]:
        """
        Getter поля phones
        (Cписок телефонных номеров организации и другая контактная информация.)

        :rtype: List[Phones] Список телефонных номеров организации и другая контактная информация.
        :return: возвращает значение поля phones
        """

        return self.__phones

    def set_phones(self, phones: List[Dict]):
        """
        Setter поля phones
        (Список телефонных номеров организации и другая контактная информация.)

        :type phones: List[Dict]
        :param phones: Список телефонных номеров организации и другая контактная информация.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_phones(phones)

    def del_phones(self) -> None:
        """
        Deleter поля phones
        (Список телефонных номеров организации и другая контактная информация.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__phones: List[Phone] = []

    def get_hours(self) -> Hours | None:
        """
        Getter поля hours
        (Режим работы организации.)

        :rtype: List[Phones] Режим работы организации.
        :return: возвращает значение поля hours
        """

        return self.__hours

    def set_hours(self, hours: List[Dict]) -> None:
        """
        Setter поля hours
        (Режим работы организации.)

        :type hours: List[Dict]
        :param hours: Режим работы организации.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_hours(hours)

    def del_hours(self):
        """
        Deleter поля hours
        (Режим работы организации.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__hours: Hours | None = None
