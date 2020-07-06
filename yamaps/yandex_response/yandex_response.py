
from typing import Dict
from typing import List

from .base.base import DestructObject
from .exceptions.exceptions import MissingRequiredProperty
from .response_meta_data.response_meta_data import ResponseMetaData
from .feature.feature import Feature


class YandexResponse(DestructObject):
    
    def __init__(self, context: Dict) -> None:
        self.__response_meta_data: ResponseMetaData | None = None
        self.__features: List[Feature] = []
        super(YandexResponse, self).__init__(context)

    def _destruct(self) -> None:
        properties: Dict = self._context.get("properties")
        if properties:
            self.__destruct_response_meta_data(properties.get("ResponseMetaData"))
        self.__destruct_features(self._context.get("features"))

    def __destruct_response_meta_data(self, response_meta_data_context) -> None:
        if response_meta_data_context:
            self.__response_meta_data: ResponseMetaData | None = ResponseMetaData(response_meta_data_context)

    def __destruct_features(self, features_context: Dict) -> None:
        if features_context:
            self.__features: List[Feature] = [Feature(feature) for feature in features_context]

    def get_response_meta_data(self) -> ResponseMetaData:
        if self.__response_meta_data:
            return self.__response_meta_data
        else:
            raise MissingRequiredProperty(self.set_response_meta_data)

    def set_response_meta_data(self, response_meta_data: Dict) -> None:
        self.__destruct_response_meta_data(response_meta_data)

    def del_response_meta_data(self) -> None:
        self.__response_meta_data: ResponseMetaData | None = None

    def get_features(self) -> List[Feature]:
        if self.__features:
            return self.__features
        else:
            raise MissingRequiredProperty(self.set_features)

    def set_features(self, features: Dict) -> None:
        self.__destruct_features(features)

    def del_features(self) -> None:
        self.__features: List[Feature] = []

    response_meta_data = property(get_response_meta_data, set_response_meta_data, del_response_meta_data, doc="")
    features = property(get_features, set_features, del_features, doc="")



