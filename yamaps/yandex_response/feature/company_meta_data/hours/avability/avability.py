
from typing import Dict
from typing import List
from typing import Set
from yandex_response.base.base import DestructObject


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
