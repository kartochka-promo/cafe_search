
from typing import Dict
from yandex_response.base.base import DestructObject
from yandex_response.exceptions.exceptions import MissingRequiredProperty


class Category(DestructObject):
    """
    Класс, описывающий категорию в которую входит организаця,
    который конструируется из полученного объекта YandexMapsApi
    Не обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса category

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__cls: str = ""
        self.__name: str | None = None
        super(Category, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__cls: str = self._context.get("class")
        self.__name: str | None = self._context.get("name")

    def get_cls(self) -> str:
        """
        Getter поля cls
        (Класс категории предприятия. Не обязательное поле.)

        :rtype: str Класс категории предприятия. Не обязательное поле.
        :return: возвращает значение поля cls
        """

        return self.__cls

    def set_cls(self, cls: str) -> None:
        """
        Setter поля cls
        (Класс категории предприятия. Не обязательное поле.)

        :type cls: str
        :param cls: (Класс категории предприятия. Не обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__cls: str = cls

    def del_cls(self) -> None:
        """
        Deleter поля cls
        (Класс категории предприятия. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__cls: str = ""

    def get_name(self) -> str:
        """
        Getter поля name
        (Название категории предприятия. Обязательное поле.)

        :rtype: str Название категории предприятия. Обязательное поле.
        :return: возвращает значение поля name
        """

        if self.__name:
            return self.__name
        else:
            raise MissingRequiredProperty(self.set_name)

    def set_name(self, name: str | None) -> None:
        """
        Setter поля cls
        (Название категории предприятия. Обязательное поле.)

        :type name: str
        :param name: (Название категории предприятия. Обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__name: str | None = name

    def del_name(self) -> None:
        """
        Deleter поля name
        (Название категории предприятия. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__name: str | None = None

    cls = property(get_cls, set_cls, del_cls, doc="")
    name = property(get_name, set_name, del_name, doc="")
