
from typing import Dict
from typing import List

from yamaps.yandex_response.base.base import DestructObject
from yamaps.yandex_response.exceptions.exceptions import MissingRequiredProperty
from yamaps.yandex_response.response_meta_data.response_meta_data import ResponseMetaData
from yamaps.yandex_response.feature.feature import Feature


class YandexResponse(DestructObject):
    """
    Класс, описывающий ответ YandexMapsAPI.
    Конструируется из полученного объекта при запросе поиска организаций
    Обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """

    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса YandexResponse

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__response_meta_data: ResponseMetaData or None = None
        self.__features: List[Feature] = []
        super(YandexResponse, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(self._context) is dict:
            properties: Dict = self._context.get("properties")
            if type(properties) is dict:
                self.__destruct_response_meta_data(properties.get("ResponseMetaData"))

            self.__destruct_features(self._context.get("features"))

    def __destruct_response_meta_data(self, response_meta_data_context) -> None:
        """
        Метод, котрый разбирает контекст
        для response_meta_data, на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(response_meta_data_context) is dict:
            self.__response_meta_data: ResponseMetaData or None = ResponseMetaData(response_meta_data_context)

    def __destruct_features(self, features_context: Dict) -> None:
        """
        Метод, котрый разбирает контекст
        для features, на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        if type(features_context) is list:
            self.__features: List[Feature] = [Feature(feature) for feature in features_context]

    def _get_response_meta_data(self) -> ResponseMetaData:
        """
        Getter поля response_meta_data
        (Метаданные, описывающие запрос и ответ. Обязательное поле.)

        :rtype: ResponseMetaData Метаданные, описывающие запрос и ответ. Обязательное поле.
        :return: возвращает значение поля response_meta_data
        """

        if self.__response_meta_data:
            return self.__response_meta_data
        else:
            raise MissingRequiredProperty(self._set_response_meta_data)

    def _set_response_meta_data(self, response_meta_data: Dict) -> None:
        """
        Setter поля response_meta_data
        (Метаданные, описывающие запрос и ответ. Обязательное поле.)

        :type response_meta_data: Dict
        :param response_meta_data: Метаданные, описывающие запрос и ответ. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_response_meta_data(response_meta_data)

    def _del_response_meta_data(self) -> None:
        """
        Deleter поля response_meta_data
        (Метаданные, описывающие запрос и ответ. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__response_meta_data: ResponseMetaData or None = None

    def _get_features(self) -> List[Feature]:
        """
        Getter поля features
        (Контейнер результатов поиска. Обязательное поле.)

        :rtype: List[Feature] Контейнер результатов поиска. Обязательное поле.
        :return: возвращает значение поля features
        """

        if self.__features:
            return self.__features
        else:
            raise MissingRequiredProperty(self._set_features)

    def _set_features(self, features: Dict) -> None:
        """
        Setter поля response_meta_data
        (Контейнер результатов поиска. Обязательное поле.)

        :type features: Dict
        :param features: Контейнер результатов поиска. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_features(features)

    def _del_features(self) -> None:
        """
        Deleter поля features
        (Контейнер результатов поиска. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращаетs
        """

        self.__features: List[Feature] = []

    response_meta_data = property(_get_response_meta_data, _set_response_meta_data, _del_response_meta_data,
                                  doc="Метаданные, описывающие запрос и ответ. Обязательное поле.")

    features = property(_get_features, _set_features, _del_features,
                        doc="(Контейнер результатов поиска. Обязательное поле.")
