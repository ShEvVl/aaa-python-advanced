import keyword
from typing import Any, Dict


class ColorizeMixin:
    """`ColorizeMixin` миксин для определение строкового представления

    Methods:
    --------
        `__init_subclass__` - установки значения по умолчанию\n
        `colored_repr` - цветное форматирование
    """

    repr_color_code: int = 33  # Yellow by default

    def __init_subclass__(cls, **kwargs) -> None:
        """Установка значения по умолчанию атрибута `repr_color_code`
        в подклассах, если они явно не определены"""
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "repr_color_code"):
            cls.repr_color_code = ColorizeMixin.repr_color_code

    def colored_repr(self, text: str) -> str:
        """Создание строкового представления с цветным форматированием"""
        return f"\033[{self.repr_color_code}m{text}\033[0m"


class Advert(ColorizeMixin):
    """
    `Advert` класс динамически создает атрибуты экземпляра класса
    из атрибутов `JSON`-объекта

    Применен миксин `ColorizeMixin` который добавляет
    текстовое представление объектов класса `Advert`

    Methods:
    --------
        `__init__` - инициализация\n
        `__getattr__` - получение атрибута\n
        `__setattr__` - установка атрибута\n
        `price(@property)` - значение `price` как свойство\n
        `price(@price.setter)` - установка значения для свойства `price`\n
        `__str__` - определение строкового представления
    """

    def __init__(self, mapping: Dict[str, Any], is_root: bool = True) -> None:
        """
        Обработка переданного словаря.
        Если ключ является словом Python - добавляется подчеркивание (_).
        `title` - обязательный атрибут.
        """
        if is_root and "title" not in mapping:
            raise ValueError("Title is required")
        self._price: int = 0
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += "_"
            if isinstance(value, dict):
                value = Advert(value, is_root=False)
            self.__setattr__(key, value)

    def __getattr__(self, item: str) -> Any:
        """Получение атрибута"""
        return self.__dict__.get(item, 0)

    def __setattr__(self, key: str, value: Any) -> None:
        """Установка атрибута"""
        if key == "price":
            if value < 0:
                raise ValueError("Price must be >= 0")
            self._price = value
        else:
            super().__setattr__(key, value)

    @property
    def price(self) -> int:
        """Представление `price` как свойство"""
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        """Установка значения для свойства `price`"""
        if value < 0:
            raise ValueError("Price must be >= 0")
        self._price = value

    def __str__(self) -> str:
        """Определение строкового представления"""
        return self.colored_repr(f"{self.title} | {self.price} ₽")


if __name__ == "__main__":
    iphone_ad = Advert(
        {
            "title": "iPhone X",
            "price": 100,
            "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"],
            },
        }
    )
    print(iphone_ad)  # Выведет "iPhone X | 100 ₽" желтым цветом
    print(iphone_ad.price)  # Выведет 100
    print(iphone_ad.location.address)  # Выведет город Москва, Лесная, 7

    corgi = Advert({"title": "Вельш-корги", "price": 1000, "class": "dogs"})
    print(corgi.class_)  # Выведет 'dogs'
    print(corgi)  # Выведет 'Вельш-корги | 1000 ₽' желтым цветом
