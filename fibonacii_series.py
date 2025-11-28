num=8

a,b=0,1

for i in range (num):

	print(i,end=" ")
	a,b=b,a+b


# fibonacii series using recursion

def fibo(i):
	if i <= 1:
		return i

	else:
		return fibo(i - 1) + fibo(i - 2)


num = 8

for i in range(0, num ):
	print(fibo(i), end=" ")
