import csv

with open('OlympicMedals_2020.csv', encoding='utf-8') as medals:
    medals.readline().strip("\n").split(",")
    reader = csv.reader(medals)
    for data in reader:
        print(data)