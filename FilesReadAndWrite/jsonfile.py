import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

with open('jsonfile.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(languages, jsonfile)

with open('jsonfile.json', 'r') as readjson:
    data = json.load(readjson)
    print(data)
    print(data[2][1])