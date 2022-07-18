def fizz_buzz(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "fizz_buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 != 0 and num % 5 != 0:
        pass


for i in range(1, 101): 
    if(i % 3 ==0 or i % 5 ==0):
        print(i, fizz_buzz(i))