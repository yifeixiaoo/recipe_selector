import random

ingredients = ["soy sauce", "tomatoes", "noodles", "eggs", "bread", "rice", "kimchi", "onions", "potatoes", "carrots"]
recipes = []
class recipe:
  def __init__(self, name, ingredients):
    self.name = name
    self.ingredients = ingredients

  def addRecipe(self, name, ingredients):
    currRecipe = recipe(name, ingredients)
    recipes.append(currRecipe)

  addRecipe("kimchi fried rice", [])

  # checks if all the ingredients are available in order to make a specific recipe
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
    currRecipes = self.returnAllAvailableRecipes(self, allIngredients)
    randomRecipeNumber = random.randint(0, len(currRecipes) - 1)
    return currRecipes[randomRecipeNumber]

