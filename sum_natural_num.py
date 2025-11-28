# simple
n=int(input("enter the number"))
sum_n=0

for i in range (0,n+1):
	sum_n+=i

print(f"sum of natural numbers is , {sum_n}")

#using recursion
def rec_n(n):
	if n ==1:
		return 1
	else:
		return n+rec_n(n-1)

n=int(input("enter the number"))
print("sum of natural num is !",rec_n(n))