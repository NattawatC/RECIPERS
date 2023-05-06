from abc import ABCMeta, abstractmethod
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, func, Boolean

Base = declarative_base()

class RecipeModel(Base, metaclass=ABCMeta):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    duration_minute = Column(Integer)
    health_score = Column(Integer)
    serving = Column(Integer)
    image = Column(String)

    @abstractmethod
    def get_type(self):
        pass

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


print()