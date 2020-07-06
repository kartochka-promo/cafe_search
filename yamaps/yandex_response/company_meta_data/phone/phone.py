
from typing import Dict
from objects.base.base import DestructObject
from objects.exceptions.exceptions import MissingRequiredProperty


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

        self.__type: str = self._context.get("type")
        self.__formatted: str | None = self._context.get("formatted")

    def get_type(self) -> str:
        """
        Getter поля type
        Тип контактной информации (например, телефон или факс).

        :rtype: str Тип контактной информации (например, телефон или факс).
        :return: возвращает значение поля type
        """

        return self.__type

    def set_type(self, type: str) -> None:
        """
        Setter поля type
        Тип контактной информации (например, телефон или факс).

        :type type: str
        :param type: Тип контактной информации (например, телефон или факс).
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__type: str = type

    def del_type(self) -> None:
        """
        Deleter поля type
        Тип контактной информации (например, телефон или факс).

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__type: str = ""

    def get_formatted(self) -> str:
        """
        Getter поля formatted
        (Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.)

        :rtype: str Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.
        :return: возвращает значение поля formatted
        """

        if self.__formatted:
            return self.__formatted
        else:
            raise MissingRequiredProperty(self.set_formatted)

    def set_formatted(self, formatted: str | None):
        """
        Setter поля formatted
        (Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.)

        :type formatted: str | None
        :param formatted: (Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__formatted: str | None = formatted

    def del_formatted(self):
        """
        Deleter поля formatted
        (Полный номер телефона (или факса) с кодом страны и кодом города. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__formatted: str | None = None

    type = property(get_type, set_type, del_type, doc="")
    formatted = property(get_formatted, set_formatted, del_formatted, doc="")
