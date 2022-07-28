import datetime


class Account:

    @staticmethod # to make method as static don't provide self argument and annotate with @staticmethod
    def _current_time() -> datetime:
        utc_time = datetime.datetime.now()
        return utc_time

    def __init__(self, name: str, balance: float):
        self._name = name
        self.__balance = balance # to declare variable as private
        self.transaction = []

    def deposit(self, amount: int):
        self.__balance += amount
        self.show_balance()
        self.transaction.append((Account._current_time(), amount))

    def withdraw(self, amount: int):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self.show_balance()
            self.transaction.append(tuple((Account._current_time(), -amount)))
        else:
            print(f"Insufficient balance")

    def show_balance(self):
        print(f"Account balance: {self.__balance}")

    def show_transaction(self):
        print(type(self.transaction[0]))
        for time, amount in self.transaction:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
            print(f"{amount} {trans_type} at {time} ")


nithesh = Account('Nithesh', 500)
nithesh.deposit(1000)
nithesh.withdraw(2000)
nithesh.__balance = 100000 # added as separate instance variable
nithesh.show_transaction()
nithesh.withdraw(500)
nithesh.show_transaction()
print(nithesh.__dict__)
