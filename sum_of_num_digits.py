num=int(input("enter the number"))

sum_d=0

while num > 0:

	digits=num % 10
	sum_d+=digits

	num=num // 10

print("sum of the number digits :" , sum_d )