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
        self.__destruct_intervals()
        self.__destruct_days()

    def __destruct_intervals(self) -> None:
        """
        Метод, котрый разбирает временные интервалы,
        находящиеся в контексте

        :rtype: None
        :return: Ничего не возвращает
        """
        if self._context.get("Intervals"):
            self.__intervals: List[List[str]] = [[interval.get("from"), interval.get("to")] for
                                                 interval in self._context.get("Intervals")]

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
        self.__type: str | None = None
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
