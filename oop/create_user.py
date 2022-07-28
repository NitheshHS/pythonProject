from user import Person

person1 = Person('Nithesh', 24, 'Bengaluru', [9972817892])
print(person1)
person1.phone_number.append(8310342653)
print('*' * 50)
print(person1)
# update user name
print('*' * 50)
person1.name = "Nithesh Gowda"
print(person1)
print('*' * 50)
person2 = Person('Pradeep', 26, 'Shivmogga', [1234567890])
print(person2)

# Print user2 information
print(person2.name)
print(person2.age)
print(person2.address)
print(person2.phone_number)
