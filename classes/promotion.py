from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        full_price = product.price * quantity
        return full_price * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        pairs = quantity // 2
        singles = quantity % 2

        return (
            pairs * (product.price * 1.5)
            + singles * product.price
        )


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        free_items = quantity // 3
        paid_items = quantity - free_items

        return paid_items * product.price