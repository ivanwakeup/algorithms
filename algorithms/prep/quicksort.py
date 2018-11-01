import random

#works by using the r as the pivot, and starting with j swapping j with i (swaps with itself on first iteration)
#incrementing i expands the "less than" partition, whereas j represents the "greater than" partition
#put the pivot in the position right after "less than" partition at end of loop!
def partition(arr, l, r):
    i = l - 1
    for j in range(l, r):
        if arr[j] <= arr[r]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

#same as above, but pick a random index between l and r and first swap arr[q] with arr[r] to follow the same algo
def randomized_partition(arr, l, r):
    i = l - 1
    q = random.randint(l, r)
    arr[q], arr[r] = arr[r], arr[q]
    for j in range(l, r):
        if arr[j] <= arr[r]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quicksort(arr, start, end):
    if start < end:
        q = randomized_partition(arr, start, end)
        quicksort(arr, start, q-1)
        quicksort(arr, q+1, end)


data = [1,2,163126,361,6,1,34,134,61,36,136,35,6,6,6,74135]

quicksort(data, 0, len(data)-1)

print(data)