import copy
import copyreg

from contents import pantry, recipes

print(pantry)
# update the dictionary
my_pantry = {"lemon": 10, "cumin": 0}
pantry.update(my_pantry)
print(pantry)

my_recipe = recipes.copy()
recipe_update = {"Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
        "chilli",
        "oil"
    ]}
my_recipe.update(recipe_update)
print(my_recipe)
print(recipes)
print("$" * 50)
my_recipe1=copy.deepcopy(recipes)
my_recipe1.update(recipe_update)
print(my_recipe1)
print(recipes)

