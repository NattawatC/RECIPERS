class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return self.name

class RecipeRepository:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

    def get_all_recipes(self):
        return self.recipes

    def get_recipe_by_name(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe

    def delete_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                self.recipes.remove(recipe)

    def update_recipe(self, name, new_recipe: Recipe):
        for recipe in self.recipes:
            if recipe.name == name:
                recipe = new_recipe
