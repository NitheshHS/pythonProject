vehicles = {
    "Honda": "Shine",
    "Hero": "Passion Pro",
    "Enfield": "Himalayan"
}
# items fn use to get in key and value pair
for manufacturer, vehicle in vehicles.items():
    print(manufacturer, vehicle, sep=":")

print("&" * 80)
# print only key
for vehicle in vehicles:
    print(vehicle)

print("&" * 80)
#print only values
for key in vehicles:
    print(vehicles[key])

print("&" * 80)
#add element to dict
vehicles["Suzuki"] = "Gixxer"
vehicles["Mahindra"] = "Mojo"

print(vehicles)
print()
#Delete an dict item
del vehicles["Mahindra"]
print(vehicles)

#Delete an non exist item
#del vehicles["mybike"]
#print(vehicles)
print()
#pop method return the delete item value and if the key is not exist throw an error
#delete using pop
value=vehicles.pop("Hero")
print(value)
print(vehicles)
print()

#if the key is not exits we can provide additional value
value1 = vehicles.pop("mybike",None)
print(value1)