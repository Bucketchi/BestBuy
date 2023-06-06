import products
from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        return product.price * (self.percent/100) * quantity


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        total = 0
        for index in range(1,quantity + 1):
            if index % 2 == 0:
                total += product.price/2
            else:
                total += product.price
        return total


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        total = 0
        for index in range(1,quantity + 1):
            if index % 3 == 0:
                continue
            else:
                total += product.price
        return total
