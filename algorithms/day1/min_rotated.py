def search(arr):
    if len(arr) == 1:
        return arr[0]
    res = 999999999
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        res = min(res, arr[mid])
        if arr[mid] < arr[end]:
            end = mid - 1
        else:
            start = mid + 1

    return res




data = [[5,6,7,2,3,4],
        [1,2,3,4,5,6,7],
        [6,7,1,2,3,4,5],
        [1],
        [0]]

print([search(x) for x in data])
