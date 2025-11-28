#calculate factorial of nth num
num = int(input("Enter a number: "))

factorial = 1

if num < 0:

	print("number zero have no factorial")

elif num == 0:

	print("factorial of zero is 1")

else:

	for i in range(1, num + 1):
		factorial *= i

print(f' factorial of {num} is : {factorial}')

#using recersion

def fact_rec(n):
	if n==1 or n==0:
		return 1
	else:
		return n * fact_rec(n-1)

n=int(input("Enter a number: "))
print(f"factorial of {n} is !",fact_rec(n))

