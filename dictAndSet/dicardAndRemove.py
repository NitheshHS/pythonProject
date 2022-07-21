small_ints = set(range(21))
print(small_ints)

small_ints.discard(99)  # won't throw any error if the value doesn't exist in set
print(small_ints)

small_ints.remove(99)  # throws an error if the value doesn't exist in set
print(small_ints)
