# Main Product class
class Product:
    def __init__(self, name, price, quantity):
        self.promotion = None
        if name != "":
            self.name = name
        else:
            raise Exception("Cannot input empty name")
        if price >= 0:
            self.price = price
        else:
            raise Exception("Cannot input negative price")
        if quantity >= 0:
            self.quantity = quantity
        else:
            raise Exception("Cannot input negative quantity")
        if quantity != 0:
            self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion.name

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        if self.promotion is not None:
            info += f", Promotion: {self.promotion.name}"
        return info

    def buy(self, quantity) -> float:
        if self.quantity - quantity < 0:
            raise Exception("Trying to buy more than is available")
        self.set_quantity(self.quantity - quantity)
        if self.promotion is not None:
            return self.promotion.apply_promotion(self, quantity)
        return quantity * self.price


# Child class of Product, for products with limited amount per purchase
class LimitedProduct(Product):
    # New variable maximum added
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    # Maximum added to info
    def show(self) -> str:
        return super().show() + f", Maximum: {self.maximum}"

    # Checks if valid amount
    def buy(self, quantity) -> float:
        if quantity > self.maximum:
            raise Exception("Trying to buy more than is allowed for this item")
        return super().buy(quantity)


class NonStockedProduct(Product):
    # Sets default quantity to 0
    def __init__(self, name, price):
        super().__init__(name, price, 0)
        self.active = True

    # Shows everything but the quantity (not relevant)
    def show(self) -> str:
        info = f"{self.name}, Price: {self.price}"
        if self.promotion is not None:
            info += f", Promotion: {self.promotion.name}"
        return info

    # No need to check if valid quantity
    def buy(self, quantity) -> float:
        if self.promotion is not None:
            return self.promotion.apply_promotion(self, quantity)
        return quantity * self.price
