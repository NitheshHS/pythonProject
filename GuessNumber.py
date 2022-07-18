secret_number = 6
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    number = int(input("Guess: "))
    guess_count = guess_count + 1
    if number == secret_number:
        print("you won!")
        break
else:
    print("you lose")
