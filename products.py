class Product:
    def __init__(self, name, price, quantity):
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

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if self.quantity - quantity < 0:
            raise Exception("Trying to buy more than is available")
        self.set_quantity(self.quantity - quantity)
        return quantity * self.price
