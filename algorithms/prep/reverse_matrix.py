def reverse_arr(arr):
    if not arr:
        return []
    mid = len(arr)//2
    l = mid - 1
    h = mid + 1
    if len(arr)%2 == 0:
        arr[mid], arr[mid-1] = arr[mid-1],arr[mid]
        l -= 1
    while l >=0 and h < len(arr):
        arr[l], arr[h] = arr[h], arr[l]
        l-=1
        h+=1
    return


data = [[1],[2],[3]]

reverse_arr(data)

print(data)