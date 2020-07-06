
from ..base.base import DestructObject
from ..exceptions.exceptions import MissingRequiredProperty
from ..company_meta_data.company_meta_data import CompanyMetaData
from .geometry.geometry import Geometry


class Feature(DestructObject):

    def __init__(self, context: dict) -> None:
        self.__company_meta_data: CompanyMetaData | None = None
        self.__geometry: Geometry | None = None
        super(Feature, self).__init__(context)

    def _destruct(self) -> None:
        self.__destruct_company_meta_data(self._context.get("CompanyMetaData"))
        self.__destruct_geometry(self._context.get("geometry"))

    def __destruct_company_meta_data(self, company_meta_data_context: dict) -> None:
        if company_meta_data_context:
            self.__company_meta_data: CompanyMetaData | None = CompanyMetaData(company_meta_data_context)

    def __destruct_geometry(self, geometry_context) -> None:
        if geometry_context:
            self.__geometry: Geometry | None = Geometry(geometry_context)

    def get_company_meta_data(self) -> CompanyMetaData:
        if self.__company_meta_data:
            return self.__company_meta_data
        else:
            raise MissingRequiredProperty(self.set_company_meta_data)

    def set_company_meta_data(self, company_meta_data: CompanyMetaData | None) -> None:
        self.__destruct_company_meta_data(company_meta_data)

    def del_company_meta_data(self) -> None:
        self.__company_meta_data: CompanyMetaData | None = None

    def get_geometry(self) -> Geometry:
        if self.__geometry:
            return self.__geometry
        else:
            raise MissingRequiredProperty(self.set_geometry)

    def set_geometry(self, geometry: Geometry | None) -> None:
        self.__destruct_geometry(geometry)

    def del_geometry(self) -> None:
        self.__geometry: Geometry | None = None

    company_meta_data = property(get_company_meta_data, set_company_meta_data, del_company_meta_data, doc="")
    geometry = property( get_geometry, set_geometry, del_geometry, doc="")
