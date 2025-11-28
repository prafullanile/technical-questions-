from abc import ABC, abstractmethod
class atm(ABC):
    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposite(self, amount):
        pass


class bank_acc(atm):

    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        print(f"current balance in account ${self.__balance}")

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"balance added succesfully ${amount} ")
        else:
            print("invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -=amount
            print(f"withdraw amount ${amount}")
        else:
            print("unsufficient balance")


b = bank_acc(1000)

b.check_balance()

b.deposite(500)
b.check_balance()

b.withdraw(777)
b.check_balance()