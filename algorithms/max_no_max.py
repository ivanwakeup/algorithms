def max(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] > j:
            j = arr[i]
    return j


print(max([1,3,6,4,5]))