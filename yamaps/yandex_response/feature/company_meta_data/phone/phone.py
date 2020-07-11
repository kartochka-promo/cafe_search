
from typing import Dict
from ....base.base import DestructObject
from ....exceptions.exceptions import MissingRequiredProperty


class Phone(DestructObject):
    """
    Класс, описывающий телефонный или факсовый номер организации.
    Конструируется из полученного объекта YandexMapsApi
    Не обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса phone

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__type: str = ""
        self.__formatted: str | None = None
        super(Phone, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """
        if type(self._context) is dict:
            self.__type: str = self._context.get("type")
            self.__formatted: str | None = self._context.get("formatted")

    def _get_type(self) -> str:
        """
        Getter поля type
        Тип контактной информации (например, телефон или факс).

        :rtype: str Тип контактной информации (например, телефон или факс).
        :return: возвращает значение поля type
        """

        return self.__type

    def _set_type(self, type: str) -> None:
        """
        Setter поля type
        Тип контактной информации (например, телефон или факс).

        :type type: str
        :param type: Тип контактной информации (например, телефон или факс).
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__type: str = type

    def _del_type(self) -> None:
        """
        Deleter поля type
        Тип контактной информации (например, телефон или факс).

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__type: str = ""

    def _get_formatted(self) -> str:
        """
        Getter поля formatted
        (Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.)

        :rtype: str Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.
        :return: возвращает значение поля formatted
        """

        if self.__formatted:
            return self.__formatted
        else:
            raise MissingRequiredProperty(self._set_formatted)

    def _set_formatted(self, formatted: str or None) -> None:
        """
        Setter поля formatted
        (Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.)

        :type formatted: str | None
        :param formatted: (Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__formatted: str | None = formatted

    def _del_formatted(self) -> None:
        """
        Deleter поля formatted
        (Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__formatted: str | None = None

    type = property(_get_type, _set_type, _del_type,
                    doc="Тип контактной информации (например, телефон или факс).")

    formatted = property(_get_formatted, _set_formatted, _del_formatted,
                         doc="Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.")
