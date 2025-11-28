def cons(arr):
    num_set = set(arr)

    longest = 0

    for num in arr:

        if num - 1 not in num_set:

            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [2, 6, 1, 9, 4, 5, 3]
print("longest consecutive order is:", cons(arr))