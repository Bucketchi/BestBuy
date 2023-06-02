import products
import pytest


def test_creating_products():
    assert products.Product("Mac", 1000, 100)


def test_creating_prod_invalid_details():
    with pytest.raises(Exception, match="Cannot input empty name"):
        products.Product("", 100, 100)
    with pytest.raises(Exception, match="Cannot input negative price"):
        products.Product("Mac", -100, 100)
    with pytest.raises(Exception, match="Cannot input negative quantity"):
        products.Product("Mac", 100, -100)


def test_prod_becomes_inactive():
    pass


pytest.main()
