 #Write a program to count even and odd numbers in a list.
list=[1,2,3,4,5,6,7,8,9]
even=0
odd=0

for i in list:

	if i%2==0:
		even+=1
	else:
		odd+=1

print(even,odd)
