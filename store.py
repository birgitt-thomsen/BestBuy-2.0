""" This module contains the Store class to hold products and allow
the user to make a purchase of multiple products at once."""


class Store:
    """ Class to hold products and allow the user to make a purchase of
    multiple products at once. """


    def __init__(self, products):
        """ Initializes the Store class with a list of products """
        self.products = products


    def add_product(self, product):
        """ Adds a product to the store """
        self.products.append(product)


    def remove_product(self, product):
        """ Removes a product from the store """
        self.products.remove(product)


    def get_total_quantity(self):
        """ Returns the total quantity of the products in the store """
        total = 0

        for product in self.products:
            total += product.get_quantity()

        return total


    def get_all_products(self):
        """ Returns a list of all active products """
        active_products = []

        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products


    def order(self, shopping_list):
        """ Orders the shopping list and returns the total price."""
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price