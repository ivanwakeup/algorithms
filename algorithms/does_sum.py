def does_sum(arr, sumto):
    arr_s = sorted(arr)
    j = len(arr) - 1
    i = 0
    while i < j:
        chk = arr_s[i] + arr_s[j]
        if chk == sumto:
            return True
        elif chk < sumto:
            i += 1
        else:
            j -= 1
    return False



print(does_sum([1,4,5,3,2], 4))