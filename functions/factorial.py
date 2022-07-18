def factorial(num: int) -> int:
    """
    Takes int number as argument and return factorial of the number
    :param num:
    :return:
    """
    fact = 1;
    for i in range(1, num + 1):
        fact = fact * i
    return fact


for i in range(1, 36):
    print(i, factorial(i))
