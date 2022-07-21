import csv

with open('cereal_grains.csv', encoding='utf-8', newline='') as cerals:
    grains = csv.reader(cerals, quoting=csv.QUOTE_NONNUMERIC)
    for value in grains:
        print(value)
