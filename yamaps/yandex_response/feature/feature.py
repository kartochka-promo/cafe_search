
from typing import Dict
from ..base.base import DestructObject
from ..exceptions.exceptions import MissingRequiredProperty
from ..company_meta_data.company_meta_data import CompanyMetaData
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

        self.__company_meta_data: CompanyMetaData | None = None
        self.__geometry: Geometry | None = None
        super(Feature, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_company_meta_data(self._context.get("CompanyMetaData"))
        self.__destruct_geometry(self._context.get("geometry"))

    def __destruct_company_meta_data(self, company_meta_data_context: dict) -> None:
        """
        Метод, котрый разбирает контекст company_meta_data,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if company_meta_data_context:
            self.__company_meta_data: CompanyMetaData | None = CompanyMetaData(company_meta_data_context)

    def __destruct_geometry(self, geometry_context) -> None:
        """
        Метод, котрый разбирает контекст geometry,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if geometry_context:
            self.__geometry: Geometry | None = Geometry(geometry_context)

    def get_company_meta_data(self) -> CompanyMetaData | None:
        """
        Getter поля company_meta_data
        (Содержит сведения об отдельной организации. Не обязательное поле)

        :rtype: CompanyMetaData | None Содержит сведения об отдельной организации. Не обязательное поле
        :return: возвращает значение поля company_meta_data
        """

        return self.__company_meta_data

    def set_company_meta_data(self, company_meta_data: Dict) -> None:
        """
        Setter поля company_meta_data
        (Содержит сведения об отдельной организации. Не обязательное поле.)

        :type company_meta_data: Dict
        :param company_meta_data: Содержит сведения об отдельной организации. Не обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_company_meta_data(company_meta_data)

    def del_company_meta_data(self) -> None:
        """
        Deleter поля company_meta_data
        (Содержит сведения об отдельной организации. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__company_meta_data: CompanyMetaData | None = None

    def get_geometry(self) -> Geometry:
        """
        Getter поля geometry
        (Описание геометрии найденного объекта. Обязательное поле.)

        :rtype: Geometry  Описание геометрии найденного объекта. Обязательное поле.
        :return: возвращает значение поля geometry
        """

        if self.__geometry:
            return self.__geometry
        else:
            raise MissingRequiredProperty(self.set_geometry)

    def set_geometry(self, geometry: Dict) -> None:
        """
        Setter поля geometry
        (Описание геометрии найденного объекта. Обязательное поле.)

        :type geometry: Dict
        :param geometry: Описание геометрии найденного объекта. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_geometry(geometry)

    def del_geometry(self) -> None:
        """
        Deleter поля geometry
        (Описание геометрии найденного объекта. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__geometry: Geometry | None = None

    company_meta_data = property(get_company_meta_data, set_company_meta_data, del_company_meta_data,
                                 doc="Содержит сведения об отдельной организации. Не обязательное поле.")

    geometry = property(get_geometry, set_geometry, del_geometry,
                        doc="Описание геометрии найденного объекта. Обязательное поле.")
