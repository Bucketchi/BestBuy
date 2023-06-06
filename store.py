# Store class
class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    # Gets the total amount of items in the store
    def get_total_quantity(self) -> int:
        quantity = 0
        for product in self.product_list:
            quantity += product.quantity
        return quantity

    # Gets the list of active products
    def get_all_products(self) -> list:
        active_list = []
        for product in self.product_list:
            if product.active:
                active_list.append(product)
        return active_list

    # Receives a shopping list of products and returns the total price
    def order(self, shopping_list) -> float:
        order_price = 0
        for product in shopping_list:
            order_price += product[0].buy(product[1])
        return order_price
