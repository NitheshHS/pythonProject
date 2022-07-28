import csv

with open('cereal_grains.csv') as cereals:
    reader = csv.DictReader(cereals)
    for values in reader:
        for cereal, fat in values.items():
            print(cereal, fat, end=", ")
