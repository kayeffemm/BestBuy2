import pytest
from classes.product import Product

def test_create_product():
    test_product = Product("Test", 1499.99, 200)
    assert isinstance(test_product, Product)


def test_create_product_empty_name():
    with pytest.raises(ValueError):
        test_product = Product("", 1499.99, 200)


def test_create_product_negative_price():
    with pytest.raises(ValueError):
        test_product = Product("Test", -500, 200)


def test_deactivate_when_zero_quantity():
    test_product = Product("Test", 1499.99, 20)
    test_product.set_quantity(0)
    assert test_product.is_active() == False


def test_update_quantity_after_buy():
    test_product = Product("Test", 1499.99, 20)
    test_product.buy(10)
    assert test_product.get_quantity() == 10


def test_exception_when_quantity_not_sufficient():
    test_product = Product("Test", 1499.99, 20)
    with pytest.raises(ValueError):
        test_product.buy(21)


pytest.main()