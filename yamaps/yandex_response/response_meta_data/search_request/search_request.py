
from ...base.base import DestructObject
from ...exceptions.exceptions import MissingRequiredProperty

import numpy as np
from typing import Dict
from typing import List


class SearchRequest(DestructObject):
    """
    Класс, описывающий метаданные, описывающие запрос.
    Конструируется из полученного объекта при запросе поиска организаций
    Обязательное поле.
    Является разбираемым объектом(DestructObject)
    https://tech.yandex.ru/maps/geosearch/doc/concepts/response_structure_business-docpage/
    """
    
    def __init__(self, context: Dict) -> None:
        """
        Конструктор класса SearchRequest

        :type context: Dict
        :param context: контекст, для разбора в объект
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__request: str | None = None
        self.__results: int | None = None
        self.__skip: int | None = None
        self.__bounded_by: List[np.array] = []
        super(SearchRequest, self).__init__(context)

    def _destruct(self) -> None:
        """
        Метод, котрый разбирает контекст,
        переданный в конструктор на составные части

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_simple_properties()
        self.__destruct_bound(self._context.get("boundedBy"))

    def __destruct_simple_properties(self) -> None:
        """
        Метод, котрый разбирает свойства контекста верхего уровня (без вложенностей),
        которые были переданны в конструктор

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__request: str | None = self._context.get("request")
        self.__results: int | None = self._context.get("results")
        self.__skip: int | None = self._context.get("skip")

    def __destruct_bound(self, bounded_by: List[List[int]]) -> None:
        """
        Метод, котрый разбирает свойство границ ответа,
        которые были переданны в конструктор

        :rtype: None
        :return: Ничего не возвращает
        """

        if bounded_by:
            self.__bounded_by = [np.array(point) for point in bounded_by]

    def get_request(self) -> str:
        """
        Getter поля request
        (Строка запроса. Обязательное поле.)

        :rtype: str Строка запроса. Обязательное поле.
        :return: возвращает значение поля request
        """

        if self.__request:
            return self.__request
        else:
            raise MissingRequiredProperty(self.set_request)

    def set_request(self, request: str | None) -> None:
        """
        Setter поля request
        (Строка запроса. Обязательное поле.)

        :type request: str | None
        :param request: Строка запроса. Обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__request: str | None = request

    def del_request(self) -> None:
        """
        Deleter поля request
        (Строка запроса. Обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__request: str | None = None

    def get_results(self) -> int | None:
        """
        Getter поля results
        (Максимальное количество возвращаемых результатов. Не обязательное поле.)

        :rtype: int Максимальное количество возвращаемых результатов. Не обязательное поле.
        :return: возвращает значение поля results
        """

        return self.__results

    def set_results(self, results: int | None) -> None:
        """
        Setter поля results
        (Максимальное количество возвращаемых результатов. Не обязательное поле.)

        :type results: int | None
        :param results: Максимальное количество возвращаемых результатов. Не обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__results: int | None = results

    def del_results(self) -> None:
        """
        Deleter поля results
        (Максимальное количество возвращаемых результатов. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__results: int | None = None

    def get_skip(self) -> int | None:
        """
        Getter поля skip
        (Количество пропускаемых результатов. Не обязательное поле.)

        :rtype: int Количество пропускаемых результатов. Не обязательное поле.
        :return: возвращает значение поля skip
        """

        return self.__skip

    def set_skip(self, skip: int | None) -> None:
        """
        Setter поля skip
        (Количество пропускаемых результатов. Не обязательное поле.)

        :type skip: int | None
        :param skip: Количество пропускаемых результатов. Не обязательное поле.
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__skip: int | None = skip

    def del_skip(self) -> None:
        """
        Deleter поля skip
        (Количество пропускаемых результатов. Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__skip: int | None = None

    def get_bounded_by(self) -> List[np.array]:
        """
        Getter поля bounded_by
        (Границы области, в которой предположительно находятся искомые объекты.
        Границы задаются в виде координат левого верхнего и
        правого нижнего углов области.
        Координаты указаны в последовательности «долгота, широта».
        Не обязательное поле.)

        :rtype: List[np.array] Границы области, в которой предположительно находятся искомые объекты. Не обязательное поле.
        :return: возвращает значение поля bounded_by
        """

        return self.__bounded_by

    def set_bounded_by(self, bounded_by: List[List[int]]) -> None:
        """
        Setter поля bounded_by
        (Границы области, в которой предположительно находятся искомые объекты.
        Границы задаются в виде координат левого верхнего и
        правого нижнего углов области.
        Координаты указаны в последовательности «долгота, широта».
        Не обязательное поле.)

        :type bounded_by: List[List[int]]
        :param bounded_by: Границы области, в которой предположительно находятся искомые объекты
        :rtype: None
        :return: Ничего не возвращает
        """

        self.__destruct_bound(bounded_by)

    def del_bounded_by(self) -> None:
        """
        Deleter поля bounded_by
        (Границы области, в которой предположительно находятся искомые объекты.
        Границы задаются в виде координат левого верхнего и
        правого нижнего углов области.
        Координаты указаны в последовательности «долгота, широта».
        Не обязательное поле.)

        :rtype: None
        :return: Ничего не возвращает
        """

        self.__bounded_by: List[np.array] = []

    request = property(get_request, set_request, del_request,
                       doc="Строка запроса. Обязательное поле.")

    results = property(get_results, set_results, del_results,
                       doc="Максимальное количество возвращаемых результатов. Не обязательное поле.")

    skip = property(get_skip, set_skip, del_skip,
                    doc="Количество пропускаемых результатов. Не обязательное поле.")

    bounded_by = property(get_bounded_by, set_bounded_by, del_bounded_by,
                          doc="Границы области, в которой предположительно находятся искомые объекты.")
