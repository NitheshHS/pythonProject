from contents import recipes, pantry

dict_recipe = {}
for index, key in enumerate(recipes):
    dict_recipe[str(index +1)] = key

print(dict_recipe)

while True:
    print("please select a recipe: ")
    for key, value in dict_recipe.items():
        print(f"{key} - {value}")
    print("press 0 to exit")
    choice = input("> ")
    if choice == '0':
        break
    elif choice in dict_recipe:
        recipe = dict_recipe[choice]
        print(f"You have selected a recipe: {recipe}")
        ingredients = recipes[recipe]
        print(f"Ingredients: {ingredients}")
        for available_item in ingredients:
           if available_item in pantry:
               print(f"{available_item}->{pantry[available_item]}")
