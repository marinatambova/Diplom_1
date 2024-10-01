import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Ketchup", 50),
    (INGREDIENT_TYPE_FILLING, "Bacon", 80),
])
def test_ingredient_get_name(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == name

@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Mustard", 40),
    (INGREDIENT_TYPE_FILLING, "Cheese", 70),
])
def test_ingredient_get_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == price

@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Mayonnaise", 45),
    (INGREDIENT_TYPE_FILLING, "Lettuce", 30),
])
def test_ingredient_get_type(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type