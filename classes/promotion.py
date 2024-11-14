from abc import ABC, abstractmethod

from classes.product import Product


class Promotion(ABC):
    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Expected name to be a string, got {type(name).__name__}.")
        if not name.strip():
            raise ValueError(f"Name can't be an empty string")
        self._name = name

    def __str__(self) -> str:
        return self._name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Every second item is only half the price.
        :param product: Takes an Object of the Product class.
        :param quantity: The amount of products the User wants to order.
        :return: a float with the new price after promotion is applied
        """
        promoted_products = quantity // 2
        non_promoted_products = quantity - promoted_products
        new_total = promoted_products * product.price / 2 + non_promoted_products * product.price
        return new_total


class ThirdOneFree(Promotion):
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Every third product ist free.
        :param product: Takes an object of the Product class.
        :param quantity: The amount of products the user wants to order.
        :return: a float with the new price after promotion is applied
        """
        promoted_products = quantity // 3
        non_promoted_products = quantity - promoted_products
        new_total = non_promoted_products * product.price
        return new_total


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float) -> None:
        super().__init__(name)

        if not isinstance(percent, (float, int)):
            raise ValueError(f"Expected percent to be int or float, got {type(percent).__name__}.")
        if percent < 0:
            raise ValueError(f"Percent can't be less than zero")
        self._percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Apply a percentage discount equal to self._percent
        :param product: Takes an object of the Product class.
        :param quantity: The amount of products the user wants to order.
        :return: a float with the new price after promotion is applied
        """
        new_total = quantity * product.price * (100 - self._percent) / 100
        return new_total
