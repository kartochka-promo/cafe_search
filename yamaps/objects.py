import numpy as np
from abc import abstractmethod

from typing import Dict
from typing import List
from typing import Any
from typing import Callable
from typing import Set


class MissingRequiredProperty(Exception):
    """
    Класс иключения, который вызывается при обращении
    к обязательному свойству объекта класса DestructObject,
    которое отсутствует. Значение можно быстро присвоить,
    воспользовавшись методом __call__.
    """

    def __init__(self, setter: Callable[[Any], None]) -> None:
        """
        Конструктор класса MissingRequiredProperty

        :type setter: Callable[[Any], None]
        :param setter: setter
        """
        property_name: str = setter.__name__.split("_")[-1]
        super(MissingRequiredProperty, self).__init__(
            f"Required property {property_name} is missing"
        )
        self.__setter: Callable[[Any], None] = setter

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        """
        Переопределение метода __call__
        делает объект класса MissingRequiredProperty callable,
        в результате чего можно сразу же вызвать обработчик, к
        оторый позволит присвоить отсутствующее значение, свойству объекта
        Пример
            try:
                print(obj.a)
            except MissingRequiredProperty as handler:
                handler("значение a")
                print(obj.a)   #выведет: значение a

        :type args: Any
        :param args: набор параметров, передаваемых в setter
        :type kwargs: Any
        :param kwargs: набор параметров, передаваемых в setter
        """
        self.__setter(*args, **kwargs)


class DestructObject:
    """ Абстрактный класс разбираемых объектов """

    def __init__(self, context: Any) -> None:
        """
        Конструктор абстрактного класса зазбираемых объектов

        :type context: Dict | List
        :param context: контекст, для разбора в объект
        """
        self._context: Any = context
        self._destruct()

    @abstractmethod
    def _destruct(self):
        """ Абстрактный метод для разборки объектов """
        pass

    @property
    def context(self) -> Dict:
        """ Getter для контекстра разбираемого объекта """
        return self._context


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


class Categories(DestructObject):

    def __init__(self, context: List[Dict]) -> None:
        self.__categories: List[Category] = []
        super(Categories, self).__init__(context)

    def _destruct(self) -> None:
        self.__destruct_categories(self._context)

    def __destruct_categories(self, categories: List) -> None:
        self.__categories: List[Category] = [Category(category) for category in categories]

    def get_categories(self) -> List[Category]:
        return self.__categories

    def set_categories(self, categories: List[Dict]) -> None:
        self.__destruct_categories(categories)

    def del_categories(self) -> None:
        self.__categories: List[Category] = []

    categories = property(get_categories, set_categories, del_categories, doc="")


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


class Phones(DestructObject):

    def __init__(self, context: List[Dict]) -> None:
        self.__phones: List[Phone] = []
        super(Phones, self).__init__(context)

    def _destruct(self) -> None:
        self.__destruct_phones(self._context)

    def __destruct_phones(self, phones) -> None:
        if phones:
            self.__phones: List[Phone] = [Phone(contact) for contact in phones]

    def get_phones(self) -> List[Phone]:
        return self.__phones

    def set_phones(self, phones) -> None:
        self.__destruct_phones(phones)

    def del_phones(self) -> None:
        self.__phones: List[Phone] = []

    phones = property(get_phones, set_phones, del_phones, doc="")


class Availability(DestructObject):
    """
    Класс, описывающий даты и время работы, найденного объекта YandexMapsApi
    Не обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса Availability

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__days: Set[str] = set()
        self.__intervals: List[List[str]] = []
        self.__twenty_four_hours: bool = False
        super(Availability, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """
        self.__destruct_intervals(self._context.get("Intervals"))
        self.__destruct_days()

    def __destruct_intervals(self, intervals: List[Dict[str, str]]) -> None:
        """
        Метод, котрый разбирает временные интервалы,
        находящиеся в контексте

        :type intervals: List[List[str]]
        :param intervals: (Интервалы работы. Не обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """
        if self._context.get("Intervals"):
            self.__intervals: List[List[str]] = [[interval.get("from"), interval.get("to")] for
                                                 interval in intervals]

        self.__twenty_four_hours: bool = not self.__intervals

    def __destruct_days(self) -> None:
        """
        Метод, котрый разбирает дни работы предприятия,
        находящиеся в контексте

        :rtype: None
        :return: Ничего не возвращает
        """

        everyday: Set[str] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
        weekdays: Set[str] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
        weekend: Set[str] = {"Saturday", "Sunday"}

        if self._context.get("Everyday"):
            self.__days: Set[str] = everyday
            return

        if self._context.get("Weekend"):
            self.__days: Set[str] = set.union(self.__days, weekend)

        if self._context.get("Weekdays"):
            self.__days: Set[str] = set.union(self.__days, weekdays)

        for day in everyday:
            if self._context.get(day):
                self.__days.add(day)

    def get_intervals(self) -> List[List[str]]:
        """
        Getter поля intervals
        (Интервалы работы. Не обязательное поле.)

        :rtype: List[List[str]]
        :return: возвращает значение поля intervals
        """
        return self.__intervals

    def set_intervals(self, intervals: List[List[str]]) -> None:
        """
        Setter поля intervals
        (Интервалы работы. Не обязательное поле.)

        :type intervals: List[List[str]]
        :param intervals: (Описание режима. Не обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """
        self.__intervals: List[List[str]] = intervals

    def del_intervals(self) -> None:
        """
        Deleter поля intervals
        (Интервалы работы. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """
        self.__intervals: List[List[str]] = []

    def get_twenty_four_hours(self) -> bool:
        """
        Getter поля twenty_four_hours
        (Круглосуточно или нет. Не обязательное поле.)

        :rtype: bool
        :return: возвращает значение поля twenty_four_hours
        """
        return self.__twenty_four_hours

    def set_twenty_four_hours(self, twenty_four_hours: bool) -> None:
        """
        Setter поля twenty_four_hours
        (Круглосуточно или нет. Не обязательное поле.)

        :type twenty_four_hours: bool
        :param twenty_four_hours: (Круглосуточно или нет. Не обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """
        self.__twenty_four_hours: bool = twenty_four_hours

    def del_twenty_four_hours(self) -> None:
        """
        Deleter поля twenty_four_hours
        (Круглосуточно или нет. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__twenty_four_hours: bool = False

    def get_days(self) -> Set[str]:
        """
        Getter поля days
        (Дни работы. Не обязательное поле.)

        :rtype: Set[str]
        :return: возвращает значение поля days
        """

        return self.__days

    def set_days(self, days: Set[str]) -> None:
        """
        Setter поля days
        (Дни работы. Не обязательное поле.)

        :type days: Set[str]
        :param days: (Дни работы. Не обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__days: Set[str] = days

    def del_days(self) -> None:
        """
        Deleter поля days
        (Дни работы. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__days: Set[str] = set()

    intervals: List[List[str]] = property(
        get_intervals, set_intervals, del_intervals, doc="Интервалы работы. Не обязательное поле.")

    twenty_four_hours: bool = property(
        get_twenty_four_hours, set_twenty_four_hours, del_twenty_four_hours,
        doc="Круглосуточно или нет. Не обязательное поле.")

    days: Set[str] = property(
        get_days, set_days, del_days,
        doc="Дни работы. Не обязательное поле.")


class Hours(DestructObject):
    """
    Класс, описывающий режим работы организации, найденного объекта YandexMapsApi
    Не обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса Hours

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """
        self.__text: str | None = None
        self.__availabilities: List[type(Availability)] = []
        super(Hours, self).__init__(context)

    def _destruct(self):
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """
        self.__text: str | None = self._context.get("text")
        self.__destruct_availabilities(self._context.get("Availabilities"))

    def __destruct_availabilities(self, availabilities: List[Dict]):
        """
        Метод, котрый разбирает контекст режима работы предприятия,
        переданный в конструктор на составные части

        :type availabilities: List[Dict]
        :param availabilities: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """
        self.__availabilities: List[type(Availability)] = \
            [Availability(availability_context) for availability_context in availabilities]

    def get_text(self):
        """
        Getter поля text
        (Описание режима работы в виде произвольного текста. Обязательное поле.)

        :rtype: str Описание режима работы в виде произвольного текста. Обязательное поле.
        :return: возвращает значение поля text
        """

        if self.__text:
            return self.__text
        else:
            raise MissingRequiredProperty(self.set_text)

    def set_text(self, text: str | None):
        """
        Setter поля text
        (Описание режима работы в виде произвольного текста. Обязательное поле.)

        :type text: str
        :param text: (Описание режима работы в виде произвольного текста. Обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__text: str | None = text

    def del_text(self):
        """
        Deleter поля text
        (Описание режима работы в виде произвольного текста. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__text: str | None = None

    def get_availabilities(self):
        """
        Getter поля availabilities
        (Описание режима работы предприятия. Не обязательное поле.)

        :rtype: List[Availability] Описание режима работы в виде произвольного текста. Обязательное поле.
        :return: возвращает значение поля availabilities
        """

        return self.__availabilities

    def set_availabilities(self, availabilities: List[Dict]):
        """
        Setter поля availabilities
        (Описание режима работы предприятия. Не обязательное поле.)

        :type availabilities: List[Availability]
        :param availabilities: (Описание режима работы в виде произвольного текста. Обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_availabilities(availabilities)

    def del_availabilities(self):
        """
        Deleter поля availabilities
        (Описание режима работы предприятия. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__availabilities: List[Availability] = []

    text: str = property(
        get_text, set_text, del_text,
        doc="Описание режима работы в виде произвольного текста. Обязательное поле.")

    availabilities: List[type(Availability)] = property(
        get_availabilities, set_availabilities, del_availabilities,
        doc="Режим работы предприятия")


class Geometry(DestructObject):
    """
    Класс описывающий геометрию найденного объекта YandexMapsApi.
    Обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса Geometry

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """
        self.__type: str | None = ""
        self.__coordinates: type(np.array) | None = None
        super(Geometry, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """
        self.__type: str | None = self._context.get("type")
        self.__coordinates: type(np.array) | None = np.array(
            self._context.get("geometry"))

    def get_type(self) -> str:
        """
        Getter поля type
        (Тип геометрии. Обязательное поле.)

        :rtype: str
        :return: возвращает значение поля type
        """
        if self.__type:
            return self.__type
        else:
            raise MissingRequiredProperty(self.set_type)

    def set_type(self, type: str) -> None:
        """
        Setter поля type
        (Тип геометрии. Обязательное поле.)

        :type type: str
        :param type: (Тип геометрии. Обязательное поле.))
        :rtype: None
        :return: Ничего не возвращает
        """
        self.__type: str | None = type

    def del_type(self) -> None:
        """
        Deleter поля type
        (Тип геометрии. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """
        self.__type: str | None = None

    def get_coordinates(self) -> np.array:
        """
        Getter поля coordinates
        (Координаты организации в последовательности «долгота, широта».
        Обязательное поле.)

        :rtype: np.array
        :return: Возвращает точку np.array
        """
        return self.__coordinates

    def set_coordinates(self, coordinates: np.array) -> None:
        """
        Setter поля coordinates
        (Координаты организации в последовательности «долгота, широта».
        Обязательное поле.)

        :type coordinates: np.array
        :param coordinates: (Координаты организации в последовательности «долгота, широта». Обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """
        self.__coordinates: type(np.array) | None = coordinates

    def del_coordinates(self) -> None:
        """
        Deleter поля coordinates
        (Координаты организации в последовательности «долгота, широта».
        Обязательное поле.)

        :rtype: np.array
        :return: Возвращает точку np.array
        """

        self.__coordinates: type(np.array) | None = None

    type: property = property(
        get_type, set_type, del_type, doc="Тип геометрии. Обязательное поле.")

    coordinates: property = property(
        get_coordinates, set_coordinates, del_coordinates,
        doc="Координаты организации в последовательности «долгота, широта».Обязательное поле.")


class CompanyMetaData(DestructObject):

    def __init__(self, context: Dict) -> None:
        self.__id: str | None = None
        self.__name: str | None = None
        self.__address: str = ""
        self.__url: str = ""
        self.__categories: Categories | None = None
        self.__phones: Phones | None = None
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
            self.__categories: Categories = Categories(categories_context)

    def __destruct_phones(self, phones_context):
        if phones_context:
            self.__phones: Phones = Phones(phones_context)

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

    def get_categories(self) -> Categories | None:
        return self.__categories

    def set_categories(self, categories: List[Dict]):
        self.__destruct_categories(categories)

    def del_categories(self) -> None:
        self.__categories: Categories | None = None

    def get_phones(self) -> Phones | None:
        return self.__phones

    def set_phones(self, phones: List[Dict]):
        self.__destruct_phones(phones)

    def del_phones(self) -> None:
        self.__phones: Phones | None = None

    def get_hours(self) -> Hours | None:
        return self.__hours

    def set_hours(self, hours: List[Dict]) -> None:
        self.__destruct_hours(hours)

    def del_hours(self):
        self.__hours: Hours | None = None




# a = {'text': 'пн-пт 9:00–18:00, перерыв 13:00–14:00', 'Availabilities':
#     [{'Intervals': [{'from': '09:00:00', 'to': '13:00:00'}, {'from': '14:00:00', 'to': '18:00:00'}],
#       'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True}]}
#
# Hours(a)

# a = {'Intervals': [{'from': '09:00:00', 'to': '13:00:00'}, {'from': '14:00:00', 'to': '18:00:00'}], 'Monday': True,
#      'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True}
# Availability(a)

# Пример (скоро уберу)
# a = Geometry({"type": "type", "geometry": [1, 2]})
#
# try:
#     print(a.type)
# except MissingRequiredProperty as handler:
#     handler(1)
#     print(a.type)
