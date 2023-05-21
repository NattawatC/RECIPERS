from abc import ABCMeta, abstractmethod

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, func, Boolean, Enum
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship, backref
from config import ENGINE as engine
from typing import List

Base = declarative_base()


class Classify(Base):
    __tablename__ = 'classify'

    recipe_id: Mapped[int] = mapped_column(Integer, ForeignKey('recipes.id'), primary_key=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('categories.category_id'), primary_key=True)
    category_type: Mapped[str] = mapped_column(String)
    category: Mapped["Category"] = relationship(back_populates="recipes", order_by="Category.category_id")
    recipe: Mapped["Recipe"] = relationship(back_populates="categories", order_by="Recipe.id")
    __mapper_args__ = {
        'polymorphic_on': category_type
    }

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # type_id = Column(Integer, ForeignKey('recipe_types.id'))
    # type = relationship("RecipeType", backref=backref('recipes'))
    categories: Mapped[List["Classify"]] = relationship(back_populates="recipe")


class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    name = Column(String)
    recipes: Mapped[List["Classify"]] = relationship(back_populates="category")

    def __repr__(self):
        return f"<Category(category_id={self.category_id}, name={self.name})>"



# class Ingredient(Base):
#     __tablename__ = 'ingredients'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     quantity = Column(String)
#     recipe_id = Column(Integer, ForeignKey('recipes.id'))
#
# class Instruction(Base):
#     __tablename__ = 'instructions'
#
#     id = Column(Integer, primary_key=True)
#     step_number = Column(Integer)
#     instruction = Column(String)
#     recipe_id = Column(Integer, ForeignKey('recipes.id'))


class Cuisine(Category):
    __tablename__ = 'cuisines'

    category_id = Column(Integer, ForeignKey('categories.category_id'), primary_key=True)
    category_type = Column(String, default='cuisine')
    __mapper_args__ = {'polymorphic_identity': 'cuisine'}

class Meal(Category):
    __tablename__ = 'meals'

    category_id = Column(Integer, ForeignKey('categories.category_id'), primary_key=True)
    category_type = Column(String, default='meal')
    __mapper_args__ = {'polymorphic_identity': 'meal'}

class Course(Category):
    __tablename__ = 'courses'

    category_id = Column(Integer, ForeignKey('categories.category_id'), primary_key=True)
    category_type = Column(String, default='course')
    __mapper_args__ = {'polymorphic_identity': 'course'}

class Condiment(Category):
    __tablename__ = 'condiments'

    category_id = Column(Integer, ForeignKey('categories.category_id'), primary_key=True)
    category_type = Column(String, default='condiment')
    __mapper_args__ = {'polymorphic_identity': 'condiment'}

class favorite_recipes(Base):
    __tablename__ = 'favorite_recipes'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    recipe = relationship("Recipe", backref=backref('favorite_recipes'))


class RecipeModel:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def getAllRecipes(self):
        recipes = self.session.query(Recipe).all()
        return recipes

    def getRecipeById(self, id):
        recipe = self.session.query(Recipe).filter_by(id=id)
        return recipe

    def getRecipeByName(self, name):
        recipe = self.session.query(Recipe).filter_by(name=name)
        return recipe

    def makeFavorite(self, user_id, recipe_id):
        favorite = favorite_recipes(user_id=user_id, recipe_id=recipe_id)
        self.session.add(favorite)
        self.session.commit()


# class RecipeRepository:
#     def __init__(self, session):
#         self.session = session


# class CategoryModel(Base):
#     __tablename__ = 'categories'
#     id = Column(Integer,primary_key=True)
#     recipe_id = Column(Integer, ForeignKey("recipes.id"))
#     type = Column(String)


# class MainDish(RecipeModel):
#     def __init__(self, name, ingredients=None, instructions=):
#         self.name = name
#
#
# class  SideDish(RecipeModel):
#     def __init__(self, name):
#         self.name = name
