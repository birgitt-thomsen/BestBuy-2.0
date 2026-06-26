""" This module contains the abstract Promotion class to facilitate the
addition and removal of specific promotions. """

from abc import ABC, abstractmethod


class Promotion(ABC):
    """ Abstract base class for promotions. """
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """ Abstract promotion method to be implemented. """
        pass


class PercentDiscount(Promotion):
    """ Promotion class that applies a percent discount to the price. """

    def __init__(self, name, percent) -> None:
        """ Initializer for percent discount class. """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """ Promotion class that applies a percent discount to the price. """
        full_price = product.price * quantity

        return full_price * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """ Promotion class that applies a second half price discount to the price. """

    def apply_promotion(self, product, quantity) -> float:
        """ Promotion class that applies a second half price discount to the price. """
        pairs = quantity // 2
        singles = quantity % 2

        return (
            pairs * (product.price * 1.5)
            + singles * product.price
        )


class ThirdOneFree(Promotion):
    """ Promotion class that applies a third one free discount to the price. """

    def apply_promotion(self, product, quantity) -> float:
        """ Promotion class that applies a third one free discount to the price. """
        free_items = quantity // 3
        paid_items = quantity - free_items

        return paid_items * product.price
