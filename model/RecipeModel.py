import time

from sqlalchemy import Column, Integer, String, ForeignKey, func, Boolean, Enum, select, or_, and_
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
    duration_minute = Column(Integer)
    name = Column(String)
    serving = Column(Integer)
    image = Column(String)
    calories = Column(Integer)
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

class Others(Category):
    __tablename__ = 'others'

    category_id = Column(Integer, ForeignKey('categories.category_id'), primary_key=True)
    category_type = Column(String, default='others')
    __mapper_args__ = {'polymorphic_identity': 'others'}

class FavoriteRecipes(Base):
    __tablename__ = 'favorite_recipes'

    user_id = Column(Integer, ForeignKey('user_info.id'), primary_key=True)

    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    user = relationship(User , backref=backref('favorite_recipes'))
    recipe = relationship(Recipe, backref=backref('favorite_recipes'))

class AddedRecipes(Base):
    __tablename__ = 'added_recipes'

    user_id = Column(Integer, ForeignKey('user_info.id'), primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    add_timestamp = Column(String)

    user = relationship(User , backref=backref('added_recipes'))
    recipe = relationship(Recipe, backref=backref('added_recipes'))


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
        favorites = []
        for id in self.session.query(FavoriteRecipes.recipe_id).filter_by(user_id=user_id).all():
            favorites.append(self.session.query(Recipe).filter_by(id=id[0]).first())
        return favorites

    def searchRecipe(self, keyword, userId):
        category = self.session.query(Category).filter_by(name=keyword).first()
        if category is not None:
            recipes = self.session.query(Recipe).join(Classify).join(Category).all()

        elif keyword.lower() == 'added':
            recipes = self.session.query(Recipe).join(AddedRecipes).filter_by(user_id=userId).all()

        elif keyword.lower() == 'favorite':
            recipes = self.session.query(Recipe).join(FavoriteRecipes).filter_by(user_id=userId).all()

        else:
            recipes = self.session.query(Recipe).filter(Recipe.name.like(f"%{keyword}%")).all()
        return recipes

    def getAddedRecipes(self, userId):
        addedRecipes = self.session.query(AddedRecipes).filter_by(user_id=userId).all()
        return addedRecipes
    
    def filterRecipe(self, tag):
        if type(tag) == str:
            recipes = self.session.query(Recipe).join(Classify).join(Category).filter_by(name=tag).all()
        
        elif type(tag) == int:
            recipes = self.session.query(Recipe).join(Classify).join(Category).filter(Recipe.serving > tag).all()

        elif type(tag) == tuple:
            if len(tag) == 2:
                if type(tag[-1]) == int and type(tag[0]) == str:
                    recipes = self.session.query(Recipe).join(Classify).join(Category).filter(or_(Recipe.name == tag[0], Recipe.serving > tag[1])).all()
                
            #condition not ok, when tuple = str,str,int
            elif len(tag) == 3 and isinstance(tag[0],str) and isinstance(tag[1],str) and isinstance(tag[-1],int):
                recipes = self.session.query(Recipe).join(Classify).join(Category).filter(or_(Recipe.name == tag[0], Recipe.name == tag[1], Recipe.serving > tag[-1])).all()
            # elif type(tag[-1]) == int and type(tag[0]) == str and type(tag[1]) == str:
            #     print("test")
            #     recipes = self.seesion.query(Recipe).join(Classify).join(Category).filter(or_(Recipe.serving > tag[2], Recipe.name == tag[0], Recipe.name == tag[1])).all()
            
            else:
                conditions = [Recipe.name == t for t in tag]
                recipes = self.session.query(Recipe).join(Classify).join(Category).filter(or_(*conditions)).all()
                
        else:
            print("else")
            recipes = self.session.query(Recipe).join(Classify).join(Category).all()
        return recipes

            
    def getAddedCount(self, userId):
        addedCount = self.session.query(AddedRecipes).filter_by(user_id=userId).count()
        return addedCount

    def createRecipe(self, recipeInfo, userId):
        recipeId = self.session.query(func.max(Recipe.id)).scalar() + 1

        addedRecipe = AddedRecipes(user_id= userId , recipe_id = recipeId ,add_timestamp=time.strftime('%Y-%m-%d %H:%M:%S'))
        self.session.add(addedRecipe)

        #Add new recipe
        recipe = Recipe(id=recipeId,
                        name=recipeInfo['detail']['name'],
                        duration_minute=recipeInfo['detail']['duration_minute'],
                        serving=recipeInfo['detail']['serving'],
                        calories=recipeInfo['detail']['calories'],
                        image=recipeInfo['detail']['image'])

        self.session.add(recipe)

        #Add ingredients
        for i in range(len(recipeInfo['ingredients'])):
            ingredientId = self.session.query(func.max(Ingredient.id)).scalar() + 1
            ingredient = Ingredient(id= ingredientId,
                                    recipe_id=recipeId,
                                    name=recipeInfo['ingredients'][i][0],
                                    amount=recipeInfo['ingredients'][i][1],
                                    unit=recipeInfo['ingredients'][i][2])
            self.session.add(ingredient)

        #Add instructions
        for i in range(len(recipeInfo['instructions'])):
            instructionId = self.session.query(func.max(Instruction.id)).scalar() + 1
            instruction = Instruction(id=instructionId,
                                      recipe_id=recipeId,
                                      step=recipeInfo['instructions'][i][0],
                                      detail=recipeInfo['instructions'][i][1])
            self.session.add(instruction)

        #Add categories
        for i in range(len(recipeInfo['categories'])):
            c = str(recipeInfo['categories'][i]).lower()
            category = self.session.query(Category).filter_by(name=c).first()
            category_type = 'other'
            if category is not None:
                if category.category_id in [5, 7, 4, 15, 11]:
                    category_type = 'meal'
                elif category.category_id  in [1, 2, 9, 10, 14, 16, 18, 20, 21]:
                    category_type = 'cuisine'
                elif category.category_id in [3, 12, 13, 19, 22, 23]:
                    category_type = 'course'
                elif category.category_id in [6, 8, 17]:
                    category_type = 'condiment'
                elif category.category_id in [U24, 25]:
                    category_type = 'beverage'
                elif category.category_id in [26]:
                    category_type = 'dessert'
                classify = Classify(recipe_id=recipeId, category_id=category.category_id, category_type=category_type)
                self.session.add(classify)

            else:
                categoryId = self.session.query(Category).count() + 1
                category = Category(name=recipeInfo['categories'][i], category_id=categoryId)
                self.session.add(category)
                classify = Classify(recipe_id=recipeId, category_id=category.category_id, category_type=category_type)
                self.session.add(classify)
        self.session.commit()

        return recipeId

    def deleteRecipe(self, RecipeId):
        try:
            classify = self.session.query(Classify).filter_by(recipe_id=RecipeId).all()
            for c in classify:
                self.session.delete(c)

            ingredient = self.session.query(Ingredient).filter_by(recipe_id=RecipeId).all()
            for i in ingredient:
                self.session.delete(i)

            instruction = self.session.query(Instruction).filter_by(recipe_id=RecipeId).all()
            for i in instruction:
                self.session.delete(i)

            addedRecipe = self.session.query(AddedRecipes).filter_by(recipe_id=RecipeId).first()
            self.session.delete(addedRecipe)

            favorite = self.session.query(FavoriteRecipes).filter_by(recipe_id=RecipeId).first()
            if favorite is not None:
                self.session.delete(favorite)

            recipe = self.session.query(Recipe).filter_by(id=RecipeId).first()
            self.session.delete(recipe)

            self.session.commit()
            return RecipeId

        except Exception as e:
            self.session.rollback()
            print(e)
            return None

    def getCreatedRecipeTime(self, userId):
        addedRecipeTime = self.session.query(AddedRecipes).filter_by(user_id=userId).all()
        return addedRecipeTime

