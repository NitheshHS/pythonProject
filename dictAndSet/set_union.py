farm_animals = {'goat', "sheep", "cow", "horse"}
wild_animals = {"lion", "leopard", "goat", "tiger", "sheep"}

new_animal_list = farm_animals.union(wild_animals)
print(new_animal_list)
# or we can use pipe operator
print(farm_animals | wild_animals)
