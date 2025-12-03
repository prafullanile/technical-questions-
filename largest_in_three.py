#Write a program to find the largest of three numbers.

a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=float(input("enter second number:"))

if a>=b and a>=c:
	print(f"a= {a} is largest in all three")
elif b>=a and b>=c:
	print(f"b= {b} is largest in all three")
else:
	print(f"c= {c} is largest in all three")