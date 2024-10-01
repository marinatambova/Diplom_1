from typing import List
from .bun import Bun
from .ingredient import Ingredient

class Burger:
    """
    Модель бургера.
    Бургер состоит из булочки и ингредиентов (начинка или соус).
    Ингредиенты можно перемещать и удалять.
    Можно распечатать чек с информацией о бургере.
    """

    def __init__(self):
        self.bun = None
        self.ingredients: List[Ingredient] = []

    def set_buns(self, bun: Bun):
        self.bun = bun

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int):
        del self.ingredients[index]

    def move_ingredient(self, index: int, new_index: int):
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    def get_price(self) -> float:
        if self.bun is None:
            price = 0
        else:
            price = self.bun.get_price() * 2

        for ingredient in self.ingredients:
            price += ingredient.get_price()

        return price

    def get_receipt(self) -> str:
        receipt: List[str] = []
        if self.bun is not None:
            receipt.append(f'(==== {self.bun.get_name()} ====)')
        else:
            receipt.append('(==== No Bun ====)')

        for ingredient in self.ingredients:
            receipt.append(f'= {ingredient.get_type().lower()} {ingredient.get_name()} =')

        if self.bun is not None:
            receipt.append(f'(==== {self.bun.get_name()} ====)\n')
        else:
            receipt.append('(==== No Bun ====)\n')

        receipt.append(f'Price: {self.get_price()}')

        return '\n'.join(receipt)
