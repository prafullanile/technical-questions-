num=int(input("enter the number"))

sum_div=0

for i in range(1,num):

	if num % i == 0:

		sum_div += i

if num == sum_div:
	print("it is the perfect number :", sum_div)

else:
        print("its Not perfect Number")