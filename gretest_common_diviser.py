a=int(input("enter first  number: "))
b=int(input("enter second number: "))

if a > b:

	md=a

else:
	md=b


for i in range(1,md+1):

	if a % i == 0 and b % i == 0:

		gcd=i

print("Gretest common diviser is :" , gcd)