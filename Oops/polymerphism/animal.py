# Polymorphism Example — Animal Sounds
# Create Animal class and subclasses like Dog, Cat, Cow.
# Each class should have a speak() method with different outputs.
# Demonstrate polymorphism by calling them in a loop.

class animal:
	def speak(self):
		pass

class dog(animal):
	def speak(self):
		return("dog is barking")

class cat(animal):
	def speak(self):
		return("cat is mouning")
class cow(animal):
	def speak(self):
		return ("cow is aamoboring")

animals=[dog(),cat(),cow()]

for animal in animals:
	print(f"{animal.__class__.__name__} says ! {animal.speak()}")
