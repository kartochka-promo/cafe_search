
from typing import Any
from typing import Callable


class MissingRequiredProperty(Exception):
    """
    Класс иключения, который вызывается при обращении
    к обязательному свойству объекта класса DestructObject,
    которое отсутствует. Значение можно быстро присвоить,
    воспользовавшись методом __call__.
    """

    def __init__(self, setter: Callable[[Any], None]) -> None:
        """
        Конструктор класса MissingRequiredProperty

        :type setter: Callable[[Any], None]
        :param setter: setter
        """
        property_name: str = setter.__name__.split("_")[-1]
        super(MissingRequiredProperty, self).__init__(
            f"Required property {property_name} is missing"
        )
        self.__setter: Callable[[Any], None] = setter

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        """
        Переопределение метода __call__
        делает объект класса MissingRequiredProperty callable,
        в результате чего можно сразу же вызвать обработчик, к
        оторый позволит присвоить отсутствующее значение, свойству объекта
        Пример
            try:
                print(obj.a)
            except MissingRequiredProperty as handler:
                handler("значение a")
                print(obj.a)   #выведет: значение a

        :type args: Any
        :param args: набор параметров, передаваемых в setter
        :type kwargs: Any
        :param kwargs: набор параметров, передаваемых в setter
        """
        self.__setter(*args, **kwargs)