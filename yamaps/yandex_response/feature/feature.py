
from typing import Dict
from ..base.base import DestructObject
from ..exceptions.exceptions import MissingRequiredProperty
from .company_meta_data.company_meta_data import CompanyMetaData
from .geometry.geometry import Geometry


class Feature(DestructObject):
    """
    Класс, описывающий контейнер результатов поиска.
    Конструируется из полученного объекта при запросе поиска организаций
    Обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: dict) -> None:
        """
        Конструктор класса Feature

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__company_meta_data: CompanyMetaData or None = None
        self.__geometry: Geometry or None = None
        self.__description: str or None = None
        self.__name: str or None = None

        super(Feature, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """
        if type(self._context) is dict:
            self.__destruct_geometry(self._context.get("geometry"))
            properties = self._context.get("properties")

            if type(properties) is dict:
                self.__destruct_simple_properties(properties)
                self.__destruct_company_meta_data(properties.get("CompanyMetaData"))

    def __destruct_simple_properties(self, properties: dict) -> None:
        """
        Метод, котрый разбирает контекст
        простых(не вложенных) полей, на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(properties) is dict:
            self.__description: str or None = properties.get("description")
            self.__name: str or None = properties.get("name")

    def __destruct_company_meta_data(self, company_meta_data_context: dict) -> None:
        """
        Метод, котрый разбирает контекст company_meta_data,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(company_meta_data_context) is dict:
            self.__company_meta_data: CompanyMetaData or None = CompanyMetaData(company_meta_data_context)

    def __destruct_geometry(self, geometry_context) -> None:
        """
        Метод, котрый разбирает контекст geometry,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(geometry_context) is dict:
            self.__geometry: Geometry or None = Geometry(geometry_context)

    def _get_name(self) -> str or None:
        """
        Getter поля name
        (Текст, который рекомендуется указывать в качестве заголовка
        при отображении найденной организации. Не обязательное поле)

        :rtype: str or None Текст, который рекомендуется указывать в качестве заголовке при отображении организации
        :return: возвращает значение поля name
        """

        return self.__name

    def _set_name(self, name: str or None) -> None:
        """
        Setter поля name
        (Текст, который рекомендуется указывать в качестве заголовка
        при отображении найденной организации. Не обязательное поле)

        :type name: str or None
        :param name: Текст, который рекомендуется указывать в качестве заголовка
            при отображении найденной организации. Не обязательное поле
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__name: str or None = name

    def _del_name(self) -> None:
        """
        Deleter поля name
        (Текст, который рекомендуется указывать в качестве заголовка
        при отображении найденной организации. Не обязательное поле)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__name: str or None = None

    def _get_description(self) -> str or None:
        """
        Getter поля description
        (Текст, который рекомендуется указывать в качестве
        подзаголовка при отображении найденной организации. Не обязательное поле)

        :rtype: str or None Текст, который рекомендуется указывать в качестве
            подзаголовка при отображении найденной организации.
        :return: возвращает значение поля description
        """

        return self.__description

    def _set_description(self, description: str or None) -> None:
        """
        Setter поля description
        (Текст, который рекомендуется указывать в качестве
        подзаголовка при отображении найденной организации. Не обязательное поле)

        :type description: str or None
        :param description: Текст, который рекомендуется указывать в качестве
            подзаголовка при отображении найденной организации. Не обязательное поле
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__description: str or None = description

    def _del_description(self) -> None:
        """
        Deleter поля description
         (Текст, который рекомендуется указывать в качестве
        подзаголовка при отображении найденной организации. Не обязательное поле)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__description: str or None = None

    def _get_company_meta_data(self) -> CompanyMetaData or None:
        """
        Getter поля company_meta_data
        (Содержит сведения об отдельной организации. Не обязательное поле)

        :rtype: CompanyMetaData | None Содержит сведения об отдельной организации. Не обязательное поле
        :return: возвращает значение поля company_meta_data
        """

        return self.__company_meta_data

    def _set_company_meta_data(self, company_meta_data: Dict) -> None:
        """
        Setter поля company_meta_data
        (Содержит сведения об отдельной организации. Не обязательное поле.)

        :type company_meta_data: Dict
        :param company_meta_data: Содержит сведения об отдельной организации. Не обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_company_meta_data(company_meta_data)

    def _del_company_meta_data(self) -> None:
        """
        Deleter поля company_meta_data
        (Содержит сведения об отдельной организации. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__company_meta_data: CompanyMetaData or None = None

    def _get_geometry(self) -> Geometry:
        """
        Getter поля geometry
        (Описание геометрии найденного объекта. Обязательное поле.)

        :rtype: Geometry  Описание геометрии найденного объекта. Обязательное поле.
        :return: возвращает значение поля geometry
        """

        if self.__geometry:
            return self.__geometry
        else:
            raise MissingRequiredProperty(self._set_geometry)

    def _set_geometry(self, geometry: Dict) -> None:
        """
        Setter поля geometry
        (Описание геометрии найденного объекта. Обязательное поле.)

        :type geometry: Dict
        :param geometry: Описание геометрии найденного объекта. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_geometry(geometry)

    def _del_geometry(self) -> None:
        """
        Deleter поля geometry
        (Описание геометрии найденного объекта. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__geometry: Geometry | None = None

    name = property(_get_name, _set_name, _del_name,
                    doc="Текст, который рекомендуется указывать в качестве заголовка "
                        "при отображении найденной организации. Не обязательное поле")

    description = property(_get_description, _set_description, _del_description,
                           doc="Текст, который рекомендуется указывать в качестве "
                               "подзаголовка при отображении найденной организации. Не обязательное поле")

    company_meta_data = property(_get_company_meta_data, _set_company_meta_data, _del_company_meta_data,
                                 doc="Содержит сведения об отдельной организации. Не обязательное поле.")

    geometry = property(_get_geometry, _set_geometry, _del_geometry,
                        doc="Описание геометрии найденного объекта. Обязательное поле.")
