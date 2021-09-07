import random

ingredients = ["soy sauce", "tomatoes", "noodles", "eggs", "bread", "rice", "kimchi", "onions", "potatoes", "carrots"]

class recipe:
  def __init__(self, ingredients):
    self.ingredients = ingredients

recipes = []

def addRecipe(ingredients):
    currRecipe = recipe(ingredients)
    recipes.append(currRecipe)


