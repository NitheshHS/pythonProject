class Car:

    def __init__(self, car_model, price):
        self._car_model = car_model
        self._price = price

    # generate getters and setters using property class
    def get_car_model(self):
        return self._car_model

    def set_car_model(self, car_model):
        self._car_model = car_model

    car_model = property(get_car_model, set_car_model)

    # generate getters and setters for price
    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    car_price = property(get_price, set_price)

    def __str__(self):
        return f"car model: {self._car_model} price: {self._price}"
