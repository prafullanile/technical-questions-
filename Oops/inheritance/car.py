# Inheritance
# Example — VehicleSystem Create
# class Vehicle(attributes: brand, speed
# Create child classes Car and Bike that inherit from Vehicle and add their own methods.


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/hr")


class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def car_details(self):
        print(f"Car Brand: {self.brand}, Speed: {self.speed} km/hr, Doors: {self.doors}")


class Bike(Vehicle):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.bike_type = bike_type

    def bike_details(self):
        print(f"Bike Brand: {self.brand}, Speed: {self.speed} km/hr, Type: {self.bike_type}")


# Example objects
c = Car("Mahindra", 180, 4)
b = Bike("Unicorn", 120, "Real World")

c.show_info()
c.car_details()

b.show_info()
b.bike_details()