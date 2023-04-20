from abc import ABCMeta

class Recipe(metaclass=ABCMeta):
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return self.name
