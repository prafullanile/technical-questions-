def my_decorator(fun):

	def wrapper():
		print("start.....")
		fun()
		print("complete.....")
	return wrapper

@my_decorator
def my_fun():
	print("block of code")

my_fun()