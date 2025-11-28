def array_ratation(arr, k):

    n=len(arr)
    k %= n

    return arr[-k:] + arr[: -k]


arr = [1, 2, 3, 4, 5]
k = 2

print("rotate array from k position:", array_ratation(arr, k))