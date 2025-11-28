def non_rep(arr):
    fq = { }

    for i in arr:
        fq[i] = fq.get(i, 0) + 1

    result = [i for i in arr if fq[i] == 1]

    return result


arr = [2, 3, 5, 6, 87, 5, 4, 32, 6]

print("non_repeatative_char_in_ arr:", non_rep(arr))