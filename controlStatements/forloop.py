number = "831,02',3278$,988*(,17377"
separator = ""
#Extracting numbers
for character in number:
    if character.isnumeric():
        separator += character;

print(separator)

separator = ""
#Extract_Special_Characters
for special in number:
    if not special.isnumeric():
        separator += special

print(separator)
print("*" * 50)
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
extract_uppercase=""
for char in quote:
    if char.isupper():
        extract_uppercase += char

print(extract_uppercase)





