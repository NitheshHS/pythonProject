class Person:

    def __init__(self, name: str, age: int, address: str, phNo: list):
        self._name = name
        self._age = age
        self._address = address
        self._phNo = phNo

    # creating getters and setters
    # creating getters and setters using decorator
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age) -> None:
        self._age = age

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, address) -> None:
        self._address = address

    @property
    def phone_number(self) -> list:
        return self._phNo

    @phone_number.setter
    def phone_number(self, phone_number) -> None:
        self._phNo = phone_number

    def __str__(self):
        return f"User created: \n name: {self._name} \n " \
               f"phone_number: {self.phone_number} \n age: {self._age} \n address: {self._address}"
