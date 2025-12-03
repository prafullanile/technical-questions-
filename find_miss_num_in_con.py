# find the missing number in the continue sequence of arr 1 to n

arr = [1, 2, 4, 5, 6]

n = len(arr) + 1

missing_value = n * (n + 1) // 2 - sum(arr)

print(missing_value)