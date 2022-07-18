name = input("Enter name? ")
age = int(input("Enter age? "))

if name and 18 <= age <=30:
    print("Hey you are welcome for holiday trip")
else:
    print(f"Sorry {name} you are not eligible for holiday trip")