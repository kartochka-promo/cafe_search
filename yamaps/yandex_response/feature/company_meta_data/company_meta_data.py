
from typing import Dict
from typing import List

from yamaps.yandex_response.base.base import DestructObject
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty

from yamaps.yandex_response.feature.company_meta_data.phone.phone import Phone
from yamaps.yandex_response.feature.company_meta_data.category.category import Category
from yamaps.yandex_response.feature.company_meta_data.hours.hours import Hours


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
        Конструктор класса company_meta_data

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__id: str or None = None
        self.__name: str or None = None
        self.__address: str or None = None
        self.__url: str or None = None
        self.__categories: List[Category] = []
        self.__phones: List[Phone] = []
        self.__hours: Hours or None = None
        super(CompanyMetaData, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(self._context) is dict:
            self.__destruct_simple_properties()
            self.__destruct_categories(self._context.get("Categories"))
            self.__destruct_phones(self._context.get("Phones"))
            self.__destruct_hours(self._context.get("Hours"))

    def __destruct_simple_properties(self) -> None:
        """
        Метод, котрый разбирает (не составные) поля
        из контекста, переданного в конструктор.

        :rtype: None
        :return: Ничего не возвращает
        """
        if type(self._context) is dict:
            self.__id: str | None = self._context.get("id")
            self.__name: str | None = self._context.get("name")
            self.__address: str or None = self._context.get("address")
            self.__url: str or None = self._context.get("url")

    def __destruct_categories(self, categories_context) -> None:
        """
        Метод, котрый разбирает составное поле categories
        из контекста, переданного в конструктор.

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(categories_context) is list:
            self.__categories: List[Category] = [Category(category) for category in categories_context]

    def __destruct_phones(self, phones_context):
        """
        Метод, котрый разбирает составное поле phones
        из контекста, переданного в конструктор.

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(phones_context) is list:
            self.__phones: List[Phone] = [Phone(contact) for contact in phones_context]

    def __destruct_hours(self, hours_context):
        """
        Метод, котрый разбирает составное поле hours
        из контекста, переданного в конструктор.

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(hours_context) is dict:
            self.__hours: Hours = Hours(hours_context)

    def _get_id(self) -> str:
        """
        Getter поля id
        (Идентификатор организации. Обязательное поле.)

        :rtype: str Идентификатор организации. Обязательное поле.
        :return: возвращает значение поля id
        """

        if self.__id:
            return self.__id
        else:
            raise MissingRequiredProperty(self._set_id)

    def _set_id(self, id: str or None) -> None:
        """
        Setter поля id
        (Идентификатор организации. Обязательное поле.)

        :type id: str
        :param id: Идентификатор организации. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__id: str | None = id

    def _del_id(self) -> None:
        """
        Deleter поля id
        (Идентификатор организации. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__id: str | None = None

    def _get_name(self) -> str:
        """
        Getter поля name
        (Название организации. Обязательное поле.)

        :rtype: str Название организации. Обязательное поле.
        :return: возвращает значение поля name
        """

        if self.__name:
            return self.__name
        else:
            raise MissingRequiredProperty(self._set_name)

    def _set_name(self, name) -> None:
        """
        Setter поля name
        (Название организации. Обязательное поле.)

        :type name: str
        :param name: Название организации. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__name: str | None = name

    def _del_name(self) -> None:
        """
        Deleter поля name
        (Название организации. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__name: str | None = None

    def _get_address(self) -> str:
        """
        Getter поля address
        (Адрес организации. Не обязательное поле.)

        :rtype: str Адрес организации. Не обязательное поле.
        :return: возвращает значение поля address
        """

        return self.__address

    def _set_address(self, address: str or None) -> None:
        """
        Setter поля address
        (Адрес организации. Не обязательное поле.)

        :type address: str
        :param address: Адрес организации. Не обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__address: str = address

    def _del_address(self) -> None:
        """
        Deleter поля address
        (Адрес организации. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__address: str or None = None

    def _get_url(self) -> str:
        """
        Getter поля url
        (Ссылка на сайт организации. Не обязательное поле.)

        :rtype: str Ссылка на сайт организации. Не обязательное поле.
        :return: возвращает значение поля url
        """

        return self.__url

    def _set_url(self, url: str or None) -> None:
        """
        Setter поля url
        (Ссылка на сайт организации. Не обязательное поле.)

        :type url: str
        :param url: Ссылка на сайт организации. Не обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__url: str or None = url

    def _del_url(self) -> None:
        """
        Deleter поля url
        (Ссылка на сайт организации. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__url: str or None = None

    def _get_categories(self) -> List[Category]:
        """
        Getter поля categories
        (Список категорий, в которые входит организация.)

        :rtype: List[category] Список категорий, в которые входит организация.
        :return: возвращает значение поля categories
        """

        return self.__categories

    def _set_categories(self, categories: List[Dict]):
        """
        Setter поля categories
        (Список категорий, в которые входит организация.)

        :type categories: List[Dict]
        :param categories: Список категорий, в которые входит организация.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_categories(categories)

    def _del_categories(self) -> None:
        """
        Deleter поля categories
        (Список категорий, в которые входит организация.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__categories: List[Category] = []

    def _get_phones(self) -> List[Phone]:
        """
        Getter поля phones
        (Cписок телефонных номеров организации и другая контактная информация.)

        :rtype: List[Phones] Список телефонных номеров организации и другая контактная информация.
        :return: возвращает значение поля phones
        """

        return self.__phones

    def _set_phones(self, phones: List[Dict]):
        """
        Setter поля phones
        (Список телефонных номеров организации и другая контактная информация.)

        :type phones: List[Dict]
        :param phones: Список телефонных номеров организации и другая контактная информация.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_phones(phones)

    def _del_phones(self) -> None:
        """
        Deleter поля phones
        (Список телефонных номеров организации и другая контактная информация.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__phones: List[Phone] = []

    def _get_hours(self) -> Hours or None:
        """
        Getter поля hours
        (Режим работы организации.)

        :rtype: List[Phones] Режим работы организации.
        :return: возвращает значение поля hours
        """

        return self.__hours

    def _set_hours(self, hours: List[Dict]) -> None:
        """
        Setter поля hours
        (Режим работы организации.)

        :type hours: List[Dict]
        :param hours: Режим работы организации.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_hours(hours)

    def _del_hours(self):
        """
        Deleter поля hours
        (Режим работы организации.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__hours: Hours or None = None

    id = property(_get_id, _set_id, _del_id,
                  doc="Идентификатор организации. Обязательное поле.")

    name = property(_get_name, _set_name, _del_name,
                    doc="Название организации. Обязательное поле.")

    address = property(_get_address, _set_address, _del_address,
                       doc="Адрес организации. Не обязательное поле.")

    url = property(_get_url, _set_url, _del_url,
                   doc="Ссылка на сайт организации. Не обязательное поле.")

    categories = property(_get_categories, _set_categories, _del_categories,
                          doc="Список категорий, в которые входит организация.")

    phones = property(_get_phones, _set_phones, _del_phones,
                      doc="Список телефонных номеров организации и другая контактная информация.")

    hours = property(_get_hours, _set_hours, _del_hours,
                     doc="Режим работы организации.")