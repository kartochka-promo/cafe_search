
from typing import Dict
from ....base.base import DestructObject
from ....exceptions.exceptions import MissingRequiredProperty


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

        self.__cls: str or None = None
        self.__name: str | None = None
        super(Category, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """
        if type(self._context) is dict:
            self.__cls: str = self._context.get("class")
            self.__name: str | None = self._context.get("name")

    def _get_cls(self) -> str or None:
        """
        Getter поля cls
        (Класс категории предприятия. Не обязательное поле.)

        :rtype: str Класс категории предприятия. Не обязательное поле.
        :return: возвращает значение поля cls
        """

        return self.__cls

    def _set_cls(self, cls: str) -> None:
        """
        Setter поля cls
        (Класс категории предприятия. Не обязательное поле.)

        :type cls: str
        :param cls: (Класс категории предприятия. Не обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__cls: str = cls

    def _del_cls(self) -> None:
        """
        Deleter поля cls
        (Класс категории предприятия. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__cls: str or None = None

    def _get_name(self) -> str:
        """
        Getter поля name
        (Название категории предприятия. Обязательное поле.)

        :rtype: str Название категории предприятия. Обязательное поле.
        :return: возвращает значение поля name
        """

        if self.__name:
            return self.__name
        else:
            raise MissingRequiredProperty(self._set_name)

    def _set_name(self, name: str or None) -> None:
        """
        Setter поля cls
        (Название категории предприятия. Обязательное поле.)

        :type name: str
        :param name: (Название категории предприятия. Обязательное поле.)
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__name: str | None = name

    def _del_name(self) -> None:
        """
        Deleter поля name
        (Название категории предприятия. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__name: str | None = None

    cls = property(_get_cls, _set_cls, _del_cls,
                   doc="Класс категории предприятия. Не обязательное поле.")

    name = property(_get_name, _set_name, _del_name,
                    doc="Название категории предприятия. Обязательное поле.")
