wild_animals = {'tiger', 'Giraffe', 'lion', 'leopard', 'deer'}

print(wild_animals)

another_wild_animals = {'lion', 'leopard', 'deer', 'tiger', 'Giraffe'}

if wild_animals == another_wild_animals:
    print("wild and another wild animals are equal")

# Adding value to the set
numbers = set()  # {*""}
print(numbers, type(numbers))

while len(numbers) < 4:
    numbers.add(input("please enter your next number: "))

print(numbers)

#Remove elements from set