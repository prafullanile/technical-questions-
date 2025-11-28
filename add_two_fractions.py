def fraction (x,y):

	gcd=1

	for i in range (1,min(x , y)+1):

		if x % i ==0 and y % i == 0:

			gcd=i

	return gcd


a=int(input("first numerator of fraction"))

b=int(input("first denomitor of fraction"))


c=int(input("second numerator of fraction"))


d=int(input("second denomitor of fraction"))


numerator=a*d + b *c
denominator=b*d


gcd=fraction(numerator,denominator)

numerator //= gcd
denominator //= gcd

print(f"sum of two fraction are :", numerator + denominator)
