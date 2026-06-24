""" This module contains the Product class to display product details and
buy a certain quantity."""

class Product:
    """ Creates a class product to handles everything about a single product"""


    def __init__(self, name, price, quantity):
        """
        Initialize a product with a name, price, and quantity.
        Raises ValueError if the name is empty or if price or quantity is
        negative.
        """
        if not name:
            raise ValueError("Name cannot be empty")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """ Returns the quantity of the product """
        return self.quantity


    def set_quantity(self, quantity):
        """ Sets the quantity of the product. Raises ValueError if the
        quantity is negative """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()


    def is_active(self):
        """ Returns whether the product is active """
        return self.active


    def activate(self):
        """ Activates the product """
        self.active = True


    def deactivate(self):
        """ Deactivates the product """
        self.active = False


    def show(self):
        """ Prints the product details"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        """ Buys the product and updates the quantity. Raises ValueError
        when the buy quantity exceeds the product quantity. """
        if self.quantity < quantity:
            raise ValueError("Insufficient quantity available")

        self.set_quantity(self.quantity - quantity)

        return float(quantity * self.price)