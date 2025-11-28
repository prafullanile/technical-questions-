
def automorphic(num):
    sq = num * num
    digit = len(str(num))
    last_digit = sq % (10 ** digit)

    if last_digit == num:
        print('automorphic')
    else:
        print('not')

num = 5
automorphic(num)
