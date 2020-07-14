
from typing import List
from typing import Dict
import numpy as np

from yamaps.yandex_response.base.base import DestructObject
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty


class SearchResponse(DestructObject):
    """
    Класс, описывающий метаданные, описывающие ответ.
    Конструируется из полученного объекта при запросе поиска организаций
    Обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса SearchResponse

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__found: int or None = None
        self.__display: str or None = None
        self.__bounded_by: List[np.array] = []
        super(SearchResponse, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(self._context) is dict:
            self.__destruct_simple_properties()
            self.__destruct_bound(self._context.get("boundedBy"))

    def __destruct_simple_properties(self) -> None:
        """
        Метод, котрый разбирает свойства контекста верхего уровня (без вложенностей),
        которые были переданны в конструктор

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(self._context) is dict:
            self.__found: int or None = self._context.get("found")
            self.__display: str or None = self._context.get("display")

    def __destruct_bound(self, bounded_by: List[List[float]]) -> None:
        """
        Метод, котрый разбирает свойство границ поиска,
        которые были переданны в конструктор

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(bounded_by) is list:
            self.__bounded_by = [np.array(point) for point in bounded_by]

    def _get_found(self) -> int:
        """
        Getter поля found
        (Количество найденных объектов. Обязательное поле.)

        :rtype: int Количество найденных объектов. Обязательное поле.
        :return: возвращает значение поля found
        """

        if self.__found:
            return self.__found
        else:
            raise MissingRequiredProperty(self._set_found)

    def _set_found(self, found: int or None) -> None:
        """
        Setter поля search_response
        (Количество найденных объектов. Обязательное поле.)

        :type found: int | None
        :param found: Количество найденных объектов. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__found: int or None = found

    def _del_found(self) -> None:
        """
        Deleter поля found
        (Количество найденных объектов. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__found: int or None = None

    def _get_bounded_by(self) -> List[np.array]:
        """
        Getter поля bounded_by
        (Границы области показа найденных объектов.
        Содержит координаты левого нижнего и правого верхнего углов области.
        Координаты указаны в последовательности «долгота, широта».)

        :rtype: List[np.array]
        :return: возвращает значение поля bounded_by
        """

        return self.__bounded_by

    def _set_bounded_by(self, bounded_by: List[List[float]]):
        """
        Setter поля search_response
        (Границы области показа найденных объектов.
        Содержит координаты левого нижнего и правого верхнего углов области.
        Координаты указаны в последовательности «долгота, широта».)

        :type bounded_by: List[List[float]]
        :param bounded_by: Границы области показа найденных объектов
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_bound(bounded_by)

    def _del_bounded_by(self) -> None:
        """
        Deleter поля bounded_by
        (Границы области показа найденных объектов.
        Содержит координаты левого нижнего и правого верхнего углов области.
        Координаты указаны в последовательности «долгота, широта».)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__bounded_by: List[np.array] = []

    def _get_display(self) -> str or None:
        """
        Getter поля display
        (Рекомендации по отображению результатов поиска)

        :rtype: List[np.array] Рекомендации по отображению результатов поиска
        :return: возвращает значение поля display
        """

        return self.__display

    def _set_display(self, display: str or None) -> None:
        """
        Setter поля display
        (Рекомендации по отображению результатов поиска)

        :type display: str | None
        :param display: Рекомендации по отображению результатов поиска
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__display: str or None = display

    def _del_display(self) -> None:
        """
        Deleter поля display
        (Рекомендации по отображению результатов поиска)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__display: str or None = None

    found = property(_get_found, _set_found, _del_found,
                     doc="Количество найденных объектов. Обязательное поле.")

    bounded_by = property(_get_bounded_by, _set_bounded_by, _del_bounded_by,
                          doc="Границы области показа найденных объектов")

    display = property(_get_display, _set_display, _del_display,
                       doc="Рекомендации по отображению результатов поиска")
