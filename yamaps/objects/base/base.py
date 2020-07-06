import numpy as np
from abc import abstractmethod

from typing import Dict
from typing import List
from typing import Any


class DestructObject:
    """ Абстрактный класс разбираемых объектов """

    def __init__(self, context: Any) -> None:
        """
        Конструктор абстрактного класса зазбираемых объектов

        :type context: Dict | List
        :param context: контекст, для разбора в объект
        """
        self._context: Any = context
        self._destruct()

    @abstractmethod
    def _destruct(self):
        """ Абстрактный метод для разборки объектов """
        pass

    @property
    def context(self) -> Dict:
        """ Getter для контекстра разбираемого объекта """
        return self._context