""" This module ties together the Product and Store classes and handles the
user interface and program execution """

import classes.products as products
import classes.store as store
import classes.promotion as promotions

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half Price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = store.Store(product_list)


def start(store_name):
    """ Starts the program by showing menu and taking user input, calling the
    respective functions to execute user selections"""
    while True:
        print("\n\tStore Menu")
        print("\t----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(store_name)

        elif choice == "2":
            show_total_quantity(store_name)

        elif choice == "3":
            make_order(store_name)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


def list_products(store_name):
    """ List all products in store"""
    # print("Listing products...")
    store_name.get_all_products()
    print("------")
    for product in store_name.get_all_products():
        product.show()
    print("------")


def show_total_quantity(store_name):
    """ Show total quantity in store"""
    print(f"Total of {store_name.get_total_quantity()} items in store")


def make_order(store_name):
    """ Displays products available in store, takes order from user and makes
    order, showing the order total. Catches ValueError when item entered is
    not valid or when order quantity exceeds available quantity"""

    # print product list
    options = store_name.get_all_products()

    print("------")
    for index, product in enumerate(options, start=1):
        print(f"{index}. ", end="")
        product.show()
    print("------")

    print("When you want to finish order, enter empty text.")

    available_products = store_name.get_all_products()
    shopping_list = []

    while True:
        product_choice = input("Which product # do you want? ")
        amount_choice = input("What amount do you want? ")

        if product_choice == "":
            break

        try:
            selected_product = available_products[int(product_choice) - 1]
            shopping_list.append((selected_product, int(amount_choice)))
            print("Product added to list!\n")
        except ValueError:
            print("Error adding product!\n")

    try:
        total_price = store_name.order(shopping_list)
        print(f"Order made! Total payment: ${total_price}")
    except ValueError as e:
        print(f"Error while making order! {e}")


if __name__ == '__main__':
    start(best_buy)
