import json

with open("temperature_anomaly.json") as climate:
    data = json.load(climate)
    print(data)

citation = data["citation"]
print(citation)
print(data["data"])

for key, value in data["data"].items():
    print(f"{key}...{value}")