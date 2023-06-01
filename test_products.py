import products
import pytest


def test_creating_products():
    assert products.Product("Mac", 1000, 100)


def test_creating_prod_invalid_details():
    pass

pytest.main()
