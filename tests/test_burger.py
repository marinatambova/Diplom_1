import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

def test_burger_set_buns():
    burger = Burger()
    mock_bun = Mock(spec=Bun)
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

def test_burger_add_ingredient():
    burger = Burger()
    mock_ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(mock_ingredient)
    assert burger.ingredients[-1] == mock_ingredient

def test_burger_remove_ingredient():
    burger = Burger()
    mock_ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0

def test_burger_move_ingredient():
    burger = Burger()
    mock_ingredient1 = Mock(spec=Ingredient)
    mock_ingredient2 = Mock(spec=Ingredient)
    burger.add_ingredient(mock_ingredient1)
    burger.add_ingredient(mock_ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == mock_ingredient2
    assert burger.ingredients[1] == mock_ingredient1

def test_burger_get_price():
    burger = Burger()
    mock_bun = Mock(spec=Bun)
    mock_bun.get_price.return_value = 1.0
    burger.set_buns(mock_bun)

    mock_ingredient1 = Mock(spec=Ingredient)
    mock_ingredient1.get_price.return_value = 0.5
    mock_ingredient2 = Mock(spec=Ingredient)
    mock_ingredient2.get_price.return_value = 0.75
    burger.add_ingredient(mock_ingredient1)
    burger.add_ingredient(mock_ingredient2)

    expected_price = 1.0 * 2 + 0.5 + 0.75  # Цена булочки * 2 + цена ингредиентов
    assert burger.get_price() == expected_price