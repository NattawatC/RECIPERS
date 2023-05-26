from sqlalchemy import Column, Integer, String, ForeignKey, func, Boolean, Enum
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship, backref
from config import ENGINE as engine
from typing import List
from model.BaseModel import Base
from model.AuthModel import User


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
    serving = Column(Integer)
    duration_minute = Column(Integer)
    image = Column(String)
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



class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    name = Column(String)
    amount = Column(String)
    unit = Column(String)

class Instruction(Base):
    __tablename__ = 'instructions'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    step = Column(Integer)
    detail = Column(String)



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

class FavoriteRecipes(Base):
    __tablename__ = 'favorite_recipes'

    user_id = Column(Integer, ForeignKey('user_info.id'), primary_key=True)

    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    user = relationship(User , backref=backref('favorite_recipes'))
    recipe = relationship(Recipe, backref=backref('favorite_recipes'))


class RecipeModel:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def getAllRecipes(self):
        recipes = self.session.query(Recipe).all()
        return recipes

    def getRecipeById(self, id):
        recipe = self.session.query(Recipe).filter_by(id=id).first()
        return recipe

    def getRecipeByName(self, name):
        recipe = self.session.query(Recipe).filter_by(name=name).first()
        return recipe

    def getIngredients(self, recipe_id):
        ingredients = self.session.query(Ingredient).filter_by(recipe_id=recipe_id).all()
        return ingredients

    def getInstructions(self, recipe_id):
        instructions = self.session.query(Instruction).filter_by(recipe_id=recipe_id).all()
        return instructions

    def makeFavorite(self, user_id , recipe_id):
        favorite = FavoriteRecipes(user_id=user_id, recipe_id=recipe_id)
        self.session.add(favorite)
        self.session.commit()

    def unFavorite(self, user_id , recipe_id):
        favorite = self.session.query(FavoriteRecipes).filter_by(user_id=user_id, recipe_id=recipe_id).first()
        self.session.delete(favorite)
        self.session.commit()

    def getFavorites(self, user_id):
        favorites = self.session.query(FavoriteRecipes).filter_by(user_id=user_id).all()
        return favorites

    def searchRecipe(self, keyword, userId):
        category = self.session.query(Category).filter_by(name=keyword).first()
        if category is not None:
            recipes = self.session.query(Recipe).join(Classify).join(Category).all()

        elif keyword == 'favorite':
            recipes = self.session.query(Recipe).join(FavoriteRecipes).filter_by(user_id=userId).all()

        else:
            recipes = self.session.query(Recipe).filter(Recipe.name.like(f"%{keyword}%")).all()
        return recipes
    
    # def filterRecipe(self, tag):
    #     categoryForFilter = self.session.query(Category).filter_by(name=tag).first()
    #     if categoryForFilter is not None:
    #         recipes = self.session.query(Recipe).join(Classify).join(Category).all()
        
    #     else:
    #         recipes = self.session.query(Recipe).filter(Recipe.name.like(f"%{tag}%")).all()
    #     return recipes
    #not finished
            
            
        

    def createRecipe(self):
        pass

