'''
generally what we want to do is:
let K be the Kth smallest element to select
assume an unsorted array input

procedure:
select a pivot in the array, P
partition the array such that all elements smaller than P appear to the left and all elements larger appear to the right
inspect the index of P, if it equals K, then return arr[P], else search the left half if  K < P, or right half if P > K

'''

data = [45,91,11,5,6,1,90]
data = [1,5,6,11,45,90,91]

#for partitioning, lets start by swapping the pivot with the last element
#then, starting from the beginning, we can create two "windows" that contain elements less than
#and elements greater than the pivot
def partition(arr, piv_idx):
    if not arr or len(arr) == 1:
        return 0
    arr[piv_idx], arr[-1] = arr[-1], arr[piv_idx]
    #keep index to represent start of greater than elements
    i = -1
    #we want to swap smaller items with the beginning of the bigger window
    for j in range(0, len(arr)-1):
        if arr[j] < arr[-1]:
            #move smaller than window forward
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
    arr[-1], arr[i+1] = arr[i+1], arr[-1]
    return i+1

import random
#recursively split the search space by only examing the appropriate part of the array
def kth_smallest(arr, k):
    q = k - 1
    if len(arr) == 1:
        return arr[0]
    pivot = random.randint(0, len(arr)-1)

    part_idx = partition(arr,pivot)
    print("searching for {}th smallest in arr {}".format(k, arr))
    print("starting pivot is {}".format(pivot))
    print("partitioned around {}".format(part_idx))

    if part_idx == q:
        return arr[part_idx]
    elif part_idx > q:
        #we need to search the left half
        return kth_smallest(arr[:part_idx], k)
    else:
        return kth_smallest(arr[part_idx+1:], k-(part_idx+1))

print(kth_smallest(data, 3))

