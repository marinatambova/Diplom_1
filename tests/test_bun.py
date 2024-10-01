import pytest
from praktikum.bun import Bun

def test_bun_get_name():
    bun = Bun("Sesame Bun", 1.0)
    assert bun.get_name() == "Sesame Bun"

def test_bun_get_price():
    bun = Bun("Sesame Bun", 1.0)
    assert bun.get_price() == 1.0

@pytest.mark.parametrize("name, price", [
    ("Sesame Bun", 1.0),
    ("Whole Grain Bun", 1.2),
    ("Gluten Free Bun", 1.5)
])
def test_bun_parameters(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price