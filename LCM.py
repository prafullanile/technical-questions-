a = 4
b = 6
max_num = max(a, b)

while True:
    if max_num % a == 0 and max_num % b == 0:
        break
    max_num += 1

print("LCM:", max_num)