import csv

cereals = [
    ['Barley', 556.0, 1.7, 32.9, 10.1, 13.8],
    ['Durum', 339.0, 5.0, 27.4, 4.09, 9.7],
    ['Fonio', 240.0, 1.0, 4.0, 1.7, 0.05],
    ['Maize', 442.0, 7.4, 37.45, 6.15, 11.03],
    ['Millet', 484.0, 2.0, 37.9, 13.4, 9.15],
    ['Oats', 231.0, 9.2, 35.1, 10.3, 3.73],
    ['Rice (Brown)', 346.0, 2.8, 38.1, 9.9, 0.8],
    ['Rice (White)', 345.0, 3.6, 37.6, 5.4, 0.1],
    ['Rye', 422.0, 2.0, 31.4, 18.2, 21.2],
    ['Sorghum', 316.0, 3.0, 37.8, 9.92, 9.15],
    ['Triticale', 338.0, 1.81, 36.6, 19.0, 0.9],
    ['Wheat', 407.0, 1.2, 27.8, 12.9, 13.8]
]

cereals_header = ['Cereal', 'Calories', 'Fat', 'Protein', 'Fibre', 'Vitamin E']

with open('write_cereal.csv', 'w', encoding='utf-8',newline='') as cereals_csv:
    write = csv.writer(cereals_csv)
    write.writerow(cereals_header)
    write.writerows(cereals)

