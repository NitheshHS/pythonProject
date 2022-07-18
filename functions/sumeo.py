def sum_eo(n: int, t: str) -> int:
    sum = 0
    if t == 'e':
        for num in range(0, n, 2):
            sum += num
    elif t == 'o':
        for num in range(1, n, 2):
            sum += num
    else:
        return -1
    return sum


print(sum_eo(10, 'e'))
print(sum_eo(7, 'o'))
print(sum_eo(11, 'spam'))
