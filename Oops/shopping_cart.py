# Online Shopping Cart
# Create two classes:
#
# Item (with name, price, and quantity)
#
# Cart (to add items and calculate total)
class Item:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class cart:
    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)
        print(f"item added {item.name} {item.quantity} successfully")

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total


it1 = Item("laptop", 30000, 2)
it2 = Item("mobile", 20000, 1)

c = cart()
c.add_items(it1)
c.add_items(it2)

total_amount = c.total_price()

print(f"total amount to pay , {total_amount}")