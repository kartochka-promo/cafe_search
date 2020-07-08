
import numpy as np
from typing import Dict
from typing import List

from ...base.base import DestructObject
from ...exceptions.exceptions import MissingRequiredProperty


class Geometry(DestructObject):
    """
    Класс описывающий геометрию найденного объекта YandexMapsApi.
    Обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса geometry

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

        if type(self._context) is dict:
            self.__destruct_simple_properties()
            self.__destruct_coordinates(self._context.get("coordinates"))

    def __destruct_simple_properties(self) -> None:
        """
        Метод, котрый разбирает простые свойства(не вложенные) из контекста,
        который передаётся в конструктор

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(self._context) is dict:
            self.__type: str | None = self._context.get("type")

    def __destruct_coordinates(self, coordinates_context: List[float]) -> None:
        """
        Метод, котрый разбирает свойство coordinates из контекста,
        который передаётся в конструктор

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(coordinates_context) is list:
            self.__coordinates: type(np.array) | None = \
                np.array(coordinates_context)

    def _get_type(self) -> str:
        """
        Getter поля type
        (Тип геометрии. Обязательное поле.)

        :rtype: str
        :return: возвращает значение поля type
        """

        if type(self.__type) is str:
            return self.__type
        else:
            raise MissingRequiredProperty(self._set_type)

    def _set_type(self, type: str) -> None:
        """
        Setter поля type
        (Тип геометрии. Обязательное поле.)

        :type type: str
        :param type: (Тип геометрии. Обязательное поле.))
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__type: str | None = type

    def _del_type(self) -> None:
        """
        Deleter поля type
        (Тип геометрии. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__type: str | None = None

    def _get_coordinates(self) -> np.array:
        """
        Getter поля coordinates
        (Координаты организации в последовательности «долгота, широта».
        Обязательное поле.)

        :rtype: np.array
        :return: Возвращает точку np.array
        """

        if type(self.__coordinates) is np.ndarray:
            return self.__coordinates
        else:
            raise MissingRequiredProperty(self._set_coordinates)

    def _set_coordinates(self, coordinates: List[float]) -> None:
        """
        Setter поля coordinates
        (Координаты организации в последовательности «долгота, широта».
        Обязательное поле.)

        :type coordinates: np.array
        :param coordinates: (Координаты организации в последовательности «долгота, широта». Обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_coordinates(coordinates)

    def _del_coordinates(self) -> None:
        """
        Deleter поля coordinates
        (Координаты организации в последовательности «долгота, широта».
        Обязательное поле.)

        :rtype: np.array
        :return: Возвращает точку np.array
        """

        self.__coordinates: type(np.array) | None = None

    type: property = property(_get_type, _set_type, _del_type,
                              doc="Тип геометрии. Обязательное поле.")

    coordinates: property = property(_get_coordinates, _set_coordinates, _del_coordinates,
                                     doc="Координаты организации.Обязательное поле.")
