def second_maximum(arr):
    f_max = float('-inf')
    s_max = float('-inf')
    
    for num in arr:


        if num > f_max:

            s_max = f_max
            f_max = num

        elif num > s_max and num != f_max:

            s_max = num

    return s_max if s_max != float('-inf') else None


arr = [10, 40, 5, 9]

print(" second Max number of array:", second_maximum(arr))