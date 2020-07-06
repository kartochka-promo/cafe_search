
from typing import Dict
from typing import List

from Objects.Base.base import DestructObject
from Objects.Exceptions.exceptions import MissingRequiredProperty
from ..Hours.Avability.avability import Availability


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
