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
        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if not isinstance(price, (int, float)):
            raise TypeError("Price must be numeric.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.promotion = None


    def get_quantity(self):
        """ Returns the quantity of the product """
        return self.quantity


    def set_quantity(self, quantity):
        """ Sets the quantity of the product. Raises ValueError if the
        quantity is negative """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity

        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self):
        """ Returns whether the product is active """
        return self.active

    def get_promotion(self):
        """Returns the current promotion"""
        return self.promotion

    def set_promotion(self, promotion):
        """Sets the promotion for this product"""
        self.promotion = promotion

    def activate(self):
        """ Activates the product """
        self.active = True

    def deactivate(self):
        """ Deactivates the product """
        self.active = False

    def show(self):
        """Prints the product details"""
        if self.promotion:
            print(
                f"{self.name}, Price: {self.price}, "
                f"Quantity: {self.quantity}, "
                f"Promotion: {self.promotion.name}"
            )
        else:
            print(
                f"{self.name}, Price: {self.price}, "
                f"Quantity: {self.quantity}"
            )


    def buy(self, quantity):
        """ Buys the product and updates the quantity. Raises ValueError
        when the buy quantity exceeds the product quantity or the buy
        quantity is negative"""
        if not isinstance(quantity, int):
            raise TypeError(
                f"Quantity of {self.name} must be an integer."
            )

        if quantity < 0:
            raise ValueError(
                f"Buy quantity of {self.name} must be positive."
            )

        if quantity > self.quantity:
            raise ValueError(
                f"Insufficient quantity of {self.name} available."
            )

        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return float(quantity * self.price)


class NonStockedProduct(Product):
    """ Creates a non-stocked product that only accepts quantity 0. """
    def __init__(self, name, price):
        super().__init__(name, price, 0)
        self.activate()  # non-stocked products should always be available

    def show(self):
        print(f"{self.name}, Price: {self.price}, Non-stocked")

    def buy(self, quantity):
        if quantity < 0:
            raise ValueError(
                f"Buy quantity of {self.name} must be positive."
            )

        return float(quantity * self.price)


class LimitedProduct(Product):
    """ Creates a limited product """
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot purchase more than {self.maximum} of {self.name}."
            )

        return super().buy(quantity)

    def show(self):
        print(
            f"{self.name}, Price: {self.price}, "
            f"Quantity: {self.quantity}, Maximum: {self.maximum}"
        )