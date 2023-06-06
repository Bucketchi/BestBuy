import products
import store
import promotions

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = store.Store(product_list)


# Shows a list of available products
def list_products(store_obj):
    print("------")
    for index, product in enumerate(store_obj.get_all_products()):
        print(f"{index + 1}. {product.show()}")
    print("------")


# Shows the total amount of objects available to purchase
def show_amount(store_obj):
    print(f"Total of {store_obj.get_total_quantity()} items in store")


# Gets a list of desired purchases from user and places the order
def make_order(store_obj):
    list_products(store_obj)
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    while True:
        product_no = input("Which product # do you want? ")
        amount = input("What amount do you want? ")
        if product_no == "" or amount == "":  # Exits if empty string entered
            break
        # Verify if entered info is valid
        try:
            shopping_list.append((store_obj.product_list[int(product_no) - 1], int(amount)))
        except ValueError:
            print("Invalid values for product number or amount")
            return

        print("Product added to list!")

    if len(shopping_list) != 0:
        try:
            print("********")
            print(f"Order made! Total payment: ${store_obj.order(shopping_list)}")
        except Exception as e:
            print(str(e))


# Starts the command line interface
def start(store_obj):
    while True:
        print("""
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit""")

        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            show_amount(store_obj)
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            quit()


if __name__ == "__main__":
    start(best_buy)
