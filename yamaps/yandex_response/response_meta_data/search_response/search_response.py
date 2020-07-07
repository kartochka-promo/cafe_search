
from typing import List
from typing import Dict
import numpy as np

from ...base.base import DestructObject
from ...exceptions.exceptions import MissingRequiredProperty


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

        self.__found: int | None = None
        self.__display: str | None = None
        self.__bounded_by: List[np.array] = []
        super(SearchResponse, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_simple_properties()
        self.__destruct_bound(self._context.get("boundedBy"))

    def __destruct_simple_properties(self) -> None:
        """
        Метод, котрый разбирает свойства контекста верхего уровня (без вложенностей),
        которые были переданны в конструктор

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__found: int | None = self._context.get("found")
        self.__display: str | None = self._context.get("display")

    def __destruct_bound(self, bounded_by: List[List[float]]) -> None:
        """
        Метод, котрый разбирает свойство границ поиска,
        которые были переданны в конструктор

        :rtype: None
        :return: Ничего не возвращает
        """

        if bounded_by:
            self.__bounded_by = [np.array(point) for point in bounded_by]

    def get_found(self) -> int:
        """
        Getter поля found
        (Количество найденных объектов. Обязательное поле.)

        :rtype: int Количество найденных объектов. Обязательное поле.
        :return: возвращает значение поля found
        """

        if self.__found:
            return self.__found
        else:
            raise MissingRequiredProperty(self.set_found)

    def set_found(self, found: int | None) -> None:
        """
        Setter поля search_response
        (Количество найденных объектов. Обязательное поле.)

        :type found: int | None
        :param found: Количество найденных объектов. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__found: int | None = found

    def del_found(self) -> None:
        """
        Deleter поля found
        (Количество найденных объектов. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__found: int | None = None

    def get_bounded_by(self) -> List[np.array]:
        """
        Getter поля bounded_by
        (Границы области показа найденных объектов.
        Содержит координаты левого нижнего и правого верхнего углов области.
        Координаты указаны в последовательности «долгота, широта».)

        :rtype: List[np.array]
        :return: возвращает значение поля bounded_by
        """

        return self.__bounded_by

    def set_bounded_by(self, bounded_by: List[List[float]]):
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

    def del_bounded_by(self) -> None:
        """
        Deleter поля bounded_by
        (Границы области показа найденных объектов.
        Содержит координаты левого нижнего и правого верхнего углов области.
        Координаты указаны в последовательности «долгота, широта».)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__bounded_by: List[np.array] = []

    def get_display(self) -> str | None:
        """
        Getter поля display
        (Рекомендации по отображению результатов поиска)

        :rtype: List[np.array] Рекомендации по отображению результатов поиска
        :return: возвращает значение поля display
        """

        return self.__display

    def set_display(self, display: str | None) -> None:
        """
        Setter поля display
        (Рекомендации по отображению результатов поиска)

        :type display: str | None
        :param display: Рекомендации по отображению результатов поиска
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__display: str | None = display

    def del_display(self) -> None:
        """
        Deleter поля display
        (Рекомендации по отображению результатов поиска)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__display: str | None = None

    found = property(get_found, set_found, del_found,
                     doc="Количество найденных объектов. Обязательное поле.")

    bounded_by = property(get_bounded_by, set_bounded_by, del_bounded_by,
                          doc="Границы области показа найденных объектов")

    display = property(get_display, set_display, del_display,
                       doc="Рекомендации по отображению результатов поиска")
