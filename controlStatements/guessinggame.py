import random
number = random.randint(1, 10)
max_try=1

while True:
    guess = int(input("Enter the number in range 10: "))
    max_try += 1
    if guess == 0 or max_try == 5:
        print(f"you have reached maximum number of try and correct answer is: {number}")
        break
    elif guess < number:
        print("Please guess higher number")
    elif guess > number:
        print("Please guess lower number")
    else:
        print("You win!")
        break


# car1 = 'BMW'
# car2 = 'Audi'
#
# if car1 == car2:
#     print("car names are same")
# else:
#     print("your guess is wrong")