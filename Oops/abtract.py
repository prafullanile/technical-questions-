from abc import ABC,abstractmethod

class car(ABC):

	@abstractmethod
	def average(self):
		pass
	@abstractmethod
	def speed(self):
		pass

class fortuner(car):
	def average(self):
		print("average of fortuner is ! 11kmlt")
	def speed(self):
		print("speed of fortuner is ! 140kmhr ")

f=fortuner()

f.average()
f.speed()

#interface

class animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class dog(animal):
    def speak(self):
        print("dog IS barking!")
class cat(animal):
    def speak(self):
        print("cat IS maowing!")


c=cat()
d=dog()

c.speak()
d.speak()