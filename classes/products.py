""" This module contains the Product class to display product details and
buy a certain quantity."""

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from classes.promotion import Promotion


class Product:
    """ Creates a class product to handles everything about a single
    product. """


    def __init__(self, name, price, quantity) -> None:
        """ Initialize a product with a name, price, and quantity.
        Raises ValueError if the name is empty or if price or quantity
        is negative. """
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


    def get_quantity(self) -> int:
        """ Returns the quantity of the product. """
        return self.quantity


    def set_quantity(self, quantity) -> None:
        """ Sets the quantity of the product. Raises ValueError if the
        quantity is negative. """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity

        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """ Returns whether the product is active. """
        return self.active

    def get_promotion(self) -> Optional["Promotion"] | None:
        """Returns the current promotion. """
        return self.promotion

    def set_promotion(self, promotion) -> None:
        """Sets the promotion for this product. """
        self.promotion = promotion

    def activate(self) -> None:
        """ Activates the product. """
        self.active = True

    def deactivate(self) -> None:
        """ Deactivates the product. """
        self.active = False

    def show(self) -> None:
        """Prints the product details. """
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


    def buy(self, quantity) -> float:
        """ Buys the product and updates the quantity. Raises ValueError
        when the buy quantity exceeds the product quantity or the buy
        quantity is negative. """
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
    def __init__(self, name, price) -> None:
        super().__init__(name, price, 0)
        self.activate()  # non-stocked products should always be available

    def show(self) -> None:
        """ Prints the product details. """
        print(f"{self.name}, Price: {self.price}, Non-stocked")

    def buy(self, quantity) -> float:
        """ Buys the product and updates the quantity. Raises ValueError
        when the quantity is negative. """
        if quantity < 0:
            raise ValueError(
                f"Buy quantity of {self.name} must be positive."
            )

        return float(quantity * self.price)


class LimitedProduct(Product):
    """ Creates a limited product. """

    def __init__(self, name, price, quantity, maximum) -> None:
        """ Initialize a limited product with a name, price, and quantity. """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        """ Buys the product and updates the quantity. Raises ValueError
        when purchase exceeds the maximum. """
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot purchase more than {self.maximum} of {self.name}."
            )

        return super().buy(quantity)

    def show(self) -> None:
        """ Prints the product details. """
        print(
            f"{self.name}, Price: {self.price}, "
            f"Quantity: {self.quantity}, Maximum: {self.maximum}"
        )
