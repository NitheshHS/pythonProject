def print_fibonnaci(startno: int, endNo: int) -> None:
    """
    Accept 2 arguments start no and end no and print all the fibbonaci series within that range
    :param startno:
    :param endNo:
    :return:
    """
    num1 = num2 = 1
    for num in range(startno, endNo):
        total = num1 + num2
        print(total)
        num1 = num2
        num2 = total


print_fibonnaci(1, 100)
