num = int(input("enter the number"))

fac = []

i = 2

while num > 1:

    if num % i == 0:
        fac.append(i)
        num //= i

    else:
        i += 1

print(fac)


