import numpy as np
from abc import abstractmethod
from typing import Dict
from typing import List
from typing import Any
from typing import Callable


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

    def __init__(self, context: Dict | List) -> None:
        """
        Конструктор абстрактного класса зазбираемых объектов

        :type context: Dict | List
        :param context: контекст, для разбора в объект
        """
        self._context: Dict | List = context
        self._destruct()

    @abstractmethod
    def _destruct(self):
        """ Абстрактный метод для разборки объектов """
        pass

    @property
    def context(self) -> Dict:
        """ Getter для контекстра разбираемого объекта """
        return self._context


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
        super(Geometry, self).__init__(context)
        self.__type: str | None = None
        self.__coordinates: type(np.array) | None = None
        self._destruct()

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """
        self.__type: str | None = self._context.get("type")
        self.__coordinates: type(np.array) | None = np.array(
            self._context["geometry"])

    def get_type(self) -> str:
        """
        Getter поля type
        (Тип геометрии. Обязательное поле.)

        :rtype: возвращает значение поля type
        :return: Ничего не возвращает
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


# Пример (скоро уберу)
# a = Geometry({"type": "type", "geometry": [1, 2]})
#
# try:
#     print(a.type)
# except MissingRequiredProperty as handler:
#     handler(1)
#     print(a.type)
