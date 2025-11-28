# Attributes: brand, model, speed
# Methods:
# accelerate(amount) → increases speed
# brake(amount) → decreases speed (but not below 0)
# display() → shows car details

class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        print(f"accelerate the car {amount} speed increase {self.speed}")

    def brake(self, amount):

        if self.speed - amount < 0:
            self.speed = 0

        else :
            self.speed -= amount
        print(f"car slowdown by {amount} speed decrease by {self.speed}")

    def display(self):
        print(f"brand of car is ! {self.brand}")
        print(f"model of car is ! {self.model}")
        print(f"initial speed of car is ! {self.speed}")


c = car("toyota", "fortuner")

c.display()
c.accelerate(50)
c.brake(20)
c.brake(70)


