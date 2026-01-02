num=12344566777

count=len(str(num))
print(count)

#without type casting
num = 12345677
count = 0
while num > 0:
    num //= 10
    count += 1

print(count)
