import pytest
from classes.products import Product


# ---------- Create Product ----------

def test_create_product_with_valid_values():
    product = Product("MacBook", 1000.0, 5)

    assert product.name == "MacBook"
    assert product.price == 1000.0
    assert product.quantity == 5
    assert product.is_active() is True


def test_create_product_with_empty_name_raises_value_error():
    with pytest.raises(ValueError, match="Name cannot be empty"):
        Product("", 100, 5)


def test_create_product_with_negative_price_raises_value_error():
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product("Laptop", -10, 5)


def test_create_product_with_negative_quantity_raises_value_error():
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        Product("Laptop", 100, -1)


def test_create_product_with_whitespace_only_name_raises_value_error():
    with pytest.raises(ValueError):
        Product("   ", 10, 5)


def test_create_product_with_non_numeric_price_raises_type_error():
    with pytest.raises(TypeError):
        Product("Book", "10", 5)


def test_create_product_with_float_quantity_raises_type_error():
    with pytest.raises(TypeError):
        Product("Book", 10, 3.5)


def test_create_product_with_zero_quantity_should_be_inactive():
    product = Product("Book", 10, 0)

    assert product.is_active() is False


# ---------- get_quantity ----------

def test_get_quantity_returns_current_quantity():
    product = Product("Phone", 500, 8)

    assert product.get_quantity() == 8


# ---------- set_quantity ----------

def test_set_quantity_updates_quantity():
    product = Product("Phone", 500, 8)

    product.set_quantity(3)

    assert product.get_quantity() == 3
    assert product.is_active() is True


def test_set_quantity_to_zero_deactivates_product():
    product = Product("Phone", 500, 8)

    product.set_quantity(0)

    assert product.get_quantity() == 0
    assert product.is_active() is False


def test_set_quantity_from_zero_to_positive_activates_product():
    product = Product("Phone", 500, 8)

    product.set_quantity(0)
    assert product.is_active() is False

    product.set_quantity(5)

    assert product.get_quantity() == 5
    assert product.is_active() is True


def test_set_negative_quantity_raises_value_error():
    product = Product("Phone", 500, 8)

    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        product.set_quantity(-1)


# ---------- activate / deactivate ----------

def test_deactivate_changes_active_status():
    product = Product("Keyboard", 50, 10)

    product.deactivate()

    assert product.is_active() is False


def test_activate_changes_active_status():
    product = Product("Keyboard", 50, 10)

    product.deactivate()
    product.activate()

    assert product.is_active() is True


def test_multiple_deactivations_keep_product_inactive():
    product = Product("Book", 10, 5)

    product.deactivate()
    product.deactivate()

    assert product.is_active() is False

# ---------- buy ----------

def test_buy_reduces_quantity_and_returns_total_price():
    product = Product("Headphones", 25.0, 10)

    total_price = product.buy(3)

    assert total_price == 75.0
    assert product.get_quantity() == 7
    assert product.is_active() is True


def test_buy_entire_stock_deactivates_product():
    product = Product("Headphones", 25.0, 5)

    total_price = product.buy(5)

    assert total_price == 125.0
    assert product.get_quantity() == 0
    assert product.is_active() is False


def test_buy_more_than_available_raises_value_error():
    product = Product("Headphones", 25.0, 5)

    with pytest.raises(ValueError, match="Insufficient quantity available"):
        product.buy(6)

    # Quantity should remain unchanged
    assert product.get_quantity() == 5
    assert product.is_active() is True


def test_buy_zero_items_returns_zero_and_quantity_unchanged():
    product = Product("Headphones", 25.0, 5)

    total_price = product.buy(0)

    assert total_price == 0.0
    assert product.get_quantity() == 5
    assert product.is_active() is True


def test_buy_one_item():
    product = Product("Mouse", 20.0, 2)

    total_price = product.buy(1)

    assert total_price == 20.0
    assert product.get_quantity() == 1


def test_buy_negative_quantity_should_raise_value_error():
    product = Product("Book", 10, 5)

    with pytest.raises(ValueError):
        product.buy(-1)


def test_buy_float_quantity_raises_type_error():
    product = Product("Book", 10, 5)

    with pytest.raises(TypeError):
        product.buy(1.5)


def test_failed_purchase_does_not_change_state():
    product = Product("Book", 10, 5)

    with pytest.raises(ValueError):
        product.buy(6)

    assert product.get_quantity() == 5
    assert product.is_active() is True


def test_large_purchase():
    product = Product("Server", 1000000, 1000000)

    total = product.buy(500000)

    assert total == 500000000000.0
    assert product.get_quantity() == 500000
