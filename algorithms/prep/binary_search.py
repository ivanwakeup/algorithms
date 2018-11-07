def binary_search(arr, l, h, v):
    if not arr:
        return -1
    if l == h:
        return l if arr[l] == v else -1

    mid = (l+h)//2

    if arr[mid] == v:
        print("found value at {} index".format(mid))
        return mid
    elif arr[mid] > v:
        return binary_search(arr, l, mid, v)
    else:
        return binary_search(arr, mid+1, h, v)

data = [1,7,19,22,155,655,3592,238522]

binary_search(data, 0, len(data)-1, 325)