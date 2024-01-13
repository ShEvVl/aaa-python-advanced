from collections.abc import Callable, Iterable
from itertools import islice
from typing import TypeVar, Generic, Tuple
from dataclasses import dataclass

T = TypeVar("T")
U = TypeVar("U")


class Seq(Generic[T]):
    """
    Класс Seq предназначен для работы с последовательностями.
    Поддерживает ленивые операции map, filter и take.

    T - тип элементов последовательности.
    """

    def __init__(self, seq: Iterable[T]):
        """
        Инициализация класса с последовательностью.

        :param seq: Последовательность элементов.
        """
        self.seq = seq

    def filter(self, f: Callable[[T], bool]) -> "Seq[T]":
        """
        Применяет функцию фильтрации к элементам последовательности.

        :param f: Функция фильтрации, возвращающая bool.
        :return: Новый объект Seq с отфильтрованной последовательностью.
        """
        return Seq(filter(f, self.seq))

    def map(self, f: Callable[[T], U]) -> "Seq[U]":
        """
        Применяет функцию трансформации к элементам последовательности.

        :param f: Функция трансформации элементов.
        :return: Новый объект Seq с трансформированной последовательностью.
        """
        return Seq(map(f, self.seq))

    def take(self, n: int) -> Tuple[T, ...]:
        """
        Возвращает первые n элементов последовательности.

        :param n: Количество элементов для возврата.
        :return: Кортеж из первых n элементов.
        """
        return tuple(islice(self.seq, n))


@dataclass
class Product:
    """
    Класс Product представляет товар с названием, категорией и ценой.
    """

    name: str
    category: str
    price: float


if __name__ == "__main__":
    # Создание списка товаров
    products = [
        Product(name="Яблоко", category="Фрукт", price=1.0),
        Product(name="Банан", category="Фрукт", price=0.5),
        Product(name="Огурец", category="Овощь", price=0.8),
        Product(name="Молоко", category="Молочка", price=1.5),
        Product(name="Сыр", category="Молочка", price=3.5),
    ]

    seq = Seq(products)
    dairy_products = (
        seq.filter(lambda p: p.category == "Молочка" and p.price < 2)
        .map(lambda p: p.name)
        .take(10)
    )
    print("Дешевые молочные продукты:", list(dairy_products))
