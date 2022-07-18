for i in range(1,11):
    for j in range(1,11):
        print(f"{i} times {j} equals to {i*j}")
    print("*" * 50)

#Continue statements
shopping_list = ['mobiles', 'headphones', 'refrigerators', 'vacuum cleaners']
for item in shopping_list:
    if item == 'vacuum cleaners':
        continue

    print(f"Buy {item}")
print("*" * 80)
#Break statements
found_index = None
Shopping_item = 'no result'
for item in range(len(shopping_list)):
    if shopping_list[item] == Shopping_item:
        found_index = item
        break

if found_index is not None:
    print(f"Item {Shopping_item} found at index {found_index}")
else:
    print(f"Item {Shopping_item} found at index {found_index}")
