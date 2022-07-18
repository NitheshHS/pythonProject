student_names = ['Nithesh',"Pradeep", "Adarsh", ]

for student in student_names:
    print(student)

print()
print(student_names[1])
print(student_names[2:3])
print(student_names[-1])

shopping_cart = ["cookies", "bread", "spam", "biscuits", "chocolate"]
another_list = shopping_cart
print(id(shopping_cart))
print(id(another_list))

shopping_cart += ["Milk"]
print(shopping_cart)
print(id(shopping_cart))
print(another_list)