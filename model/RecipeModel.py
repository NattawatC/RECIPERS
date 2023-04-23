from abc import ABCMeta
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, func, Boolean

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)



class RecipeModel(metaclass=ABCMeta):
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return self.name

