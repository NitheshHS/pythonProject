# for num in range(10, 16):
#     if num%2 == 0:
#         print(num)
#
# for i in range(0, 100, 7):
#     if i % 11 == 0 and i > 0:
#         print(i)
#         break
#     elif i > 0:
#         print(i)

for i in range(0, 20):
    if i % 3 == 0 or i % 5 == 0:
       continue
    else:
        print(i)