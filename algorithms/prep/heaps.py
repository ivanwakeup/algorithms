def max_heapify_array(arr, heap_size, i):
    left = (2*i) + 1
    right = (2*i) + 2
    largest = i
    if left <= heap_size:
        if arr[left] > arr[largest]:
            largest = left
    if right <= heap_size:
        if arr[right] > arr[largest]:
            largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify_array(arr, heap_size, largest)


def make_max_heap(arr):
    for i in range(len(arr)//2, -1, -1):
        max_heapify_array(data, len(arr)-1, i)


def heapsort(arr):
    make_max_heap(arr)
    heap_size = len(arr) - 1
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify_array(arr, heap_size, 0)


data = [1,2,3,4,5,6,56,256,245,2,2,2,34,425,123,431,6743,2347,99]

heapsort(data)

print(data)
