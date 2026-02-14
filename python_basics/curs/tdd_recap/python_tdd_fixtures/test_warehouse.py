import pytest

from warehouse import Product, Warehouse

@pytest.fixture
def products():
    return [
        Product('p1', 10),
        Product('p2', 5),
        Product('p3', 2)
    ]

def test_total_value(products):
    w = Warehouse()
    for p in products:
        w.add(p)

    assert w.total_value() == 17

def test_product_count(products):
    w = Warehouse()
    for p in products:
        w.add(p)

    assert w.product_count() == 3
