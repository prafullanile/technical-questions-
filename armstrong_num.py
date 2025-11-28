num = int(input('Enter a number: '))

sum_num = 0

order = len(str(num))

copy_n = num

while num > 0:
	digit = num % 10

	sum_num += digit ** order

	num = num // 10

if copy_n == sum_num:
	print(f"{copy_n} is amstrong number ")

else:
    print(f"{copy_n} is not amstrong number")