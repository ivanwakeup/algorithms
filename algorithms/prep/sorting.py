def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = i - 1
        j = i
        while tmp >= 0:
            if arr[j] < arr[tmp]:
                arr[j], arr[tmp] = arr[tmp], arr[j]
            j -= 1
            tmp -= 1

data1 = [3,4,2,5,1,452,6416,2436,1,0,1236,1,2,2,351,36,6]

insertion_sort(data1)

print("Insertion sort result is: {}".format(data1))


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


data = [5,347,2,325,6,236,1,0,0,1741]

merge_sort(data)

print("Merge Sort result is: {}".format(data))


