import random

recipes = []
class recipe:
  # name: name of recipe
  # ingredients: must have ingredients
  # optional: optional ingredients
  def __init__(self, name, ingredients, optional):
    self.name = name
    self.ingredients = ingredients
    self.optional = optional



class recipeList:
  # List of Recipes
  def __init__(self):
    pass
    # checks if all the ingredients are available in order to make a specific recipe
  def addRecipe(self, name, ingredients, optional):
    currRecipe = recipe(name, ingredients, optional)
    recipes.append(currRecipe)
    
  def allIngredientsHere(self, allIngredients, recipeIngredients):
    for ingredient in recipeIngredients:
      if ingredient not in allIngredients:
        return False
    return True

  # function to return all recipes that can be made with the current ingredients
  def returnAllAvailableRecipes(self, allIngredients):
    availableRecipes = []
    for recipe in recipes:
      if (self.allIngredientsHere(allIngredients, recipe.ingredients)):
        availableRecipes.append(recipe)
    return availableRecipes

  # Selects a random recipe out of the list in the "recipes" array
  # only will return a recipe if "ingredients" contains the ingredients needed to make the recipe
  def selectRandomRecipe(self, allIngredients):
    currRecipes = self.returnAllAvailableRecipes(allIngredients)
    randomRecipeNumber = random.randint(0, len(currRecipes) - 1)
    print(currRecipes[randomRecipeNumber].name)
    return currRecipes[randomRecipeNumber]