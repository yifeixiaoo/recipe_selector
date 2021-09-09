from rs import recipe
from rs import recipeList

AllIngredients = ["soy sauce", "tomatoes", "noodles", "eggs", "bread", "rice", "kimchi", "onions", "potatoes", "carrots", "oil", "curry sauce"]

rl = recipeList()
rl.addRecipe("kimchi fried rice", ["oil", "rice", "kimchi", "soy sauce"], ["onions", "eggs", "tomatoes", "chicken", "pork"])
rl.addRecipe("stir fried eggs and tomatoes", ["eggs", "tomatoes", "oil"], ["onions", "eggs", "tomatoes"])
rl.addRecipe("spaghetti", ["oil", "spaghetti", "tomatoe sauce"], ["chicken", "pork"])
rl.addRecipe("curry", ["onions", "potatoes", "carrots", "curry sauce"], ["beef", "chicken", "curry sauce"])
rl.addRecipe("omlette", ["eggs", "oil"], ["onions", "tomatoes", "chicken"])

rl.selectRandomRecipe(AllIngredients)