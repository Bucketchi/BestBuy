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
    mac = products.Product("Mac", 1000, 100)
    mac.buy(100)
    assert not mac.active


def test_buy_modifies_quantity():
    mac = products.Product("Mac", 1000, 100)
    mac.buy(50)
    assert mac.quantity == 50


def test_buy_too_much():
    with pytest.raises(Exception, match="Trying to buy more than is available"):
        mac = products.Product("Mac", 1000, 100)
        mac.buy(1000000)


pytest.main()
