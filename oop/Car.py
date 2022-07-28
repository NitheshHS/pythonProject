class Car:
    # class attribute
    fuel_type = "petrol"

    def __init__(self, make: str, price: int):
        """constructor"""
        self.make = make
        self.price = price
        self.isAutoPiolot = False

    def switch_to_auto_pilot(self):
        """method"""
        self.isAutoPiolot = True


hyundai = Car("Hyundai", 100000)
print(hyundai.make.upper())
print(hyundai.price)

tata = Car("Altroz", 750000)
print(tata.make)
print(tata.price)
print(tata.isAutoPiolot)
tata.isAutoPiolot = True
print(tata.isAutoPiolot)

print(f"{hyundai.make}={hyundai.price}, {tata.make}={tata.price}")
# tata.fuel = "petrol"
# print(tata.fuel)
# print(hyundai.fuel)

if tata.isAutoPiolot:
    print("turned on autopilot")

print(Car.fuel_type)
tata.fuel_type = "Diesel"
print(tata.fuel_type)
print(hyundai.fuel_type)
