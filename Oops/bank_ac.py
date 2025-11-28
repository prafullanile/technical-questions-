class blank_acc:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f"depostite money {amount}")

    def withdrawn(self, amount):
        if  amount<=self.balance:
            self.balance -= amount
            print(f"withdrawn money {amount}")
        else:
            print(f"insufficient balance")

    def total_balance(self):
        print(f"remaining balance {self.balance}")


b = blank_acc("prafull", 0)
b.deposite(500)
b.withdrawn(200)
b.total_balance()




# class ATM with abstract methods:deposit(), withdraw(), and check_balance()
# Thencreate a BankAccount subclass that implements these methods securely
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





