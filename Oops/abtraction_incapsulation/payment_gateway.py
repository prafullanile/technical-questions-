# E - commerce Payment
# Gateway(Interface
# Example)
# Create
# an
# interface
# PaymentGateway
# with an abstract method pay().
# Implement
# classes
# like
# PayPal, UPI, CreditCard — each
# with its own payment logic.

from abc import ABC, abstractmethod


class payment_gateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class paypal(payment_gateway):
    def pay(self, amount):
        print(f"paymanet successful using paupal ${amount}")


class UPI(payment_gateway):
    def pay(self, amount):
        print(f"payment succesfull using UPI ${amount}")


class creditcard(payment_gateway):
    def pay(self, amount):
        print(f"payment successful using ${amount}")


def payment_procced(payment_method, amount):
    payment_method.pay(amount)


p = paypal()
u = UPI()
c = creditcard()

payment_procced(p, 1000)
payment_procced(u, 2000)
payment_procced(c, 3000)
