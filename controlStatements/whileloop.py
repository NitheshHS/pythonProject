directions = ["north", "south", "east", "west"]
choose_exit = ""
while choose_exit not in directions:
    choose_exit = input("enter the direction want to exit: ")

print(f"chose a direction for exit: {choose_exit}")

i = 0
while i < 10:
    print(f"i value is {i}")
    i += 1

