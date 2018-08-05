def search(ele, array):

    if not array:
        return -1

    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if ele == array[mid]:
            return mid

        if array[start] <= array[mid]:
            if array[start] <= ele <= array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if array[mid] <= ele <= array[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


data = [[4,5,6,7,1,2,3],
        [2,3,4,5,6,7,1],
        [6,7,1,2,3,4,5],
        [1],
        [0]]

print([search(1, x) for x in data])