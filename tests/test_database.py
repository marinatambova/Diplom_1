import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

def test_database_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3
    assert all(isinstance(bun, Bun) for bun in buns)
    names = [bun.get_name() for bun in buns]
    expected_names = ["black bun", "white bun", "red bun"]
    assert names == expected_names

def test_database_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    assert all(isinstance(ing, Ingredient) for ing in ingredients)
    names = [ing.get_name() for ing in ingredients]
    expected_names = [
        "hot sauce", "sour cream", "chili sauce",
        "cutlet", "dinosaur", "sausage"
    ]
    assert names == expected_names