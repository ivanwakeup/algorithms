'''
partition function:

we want to partition an array by choosing some pivot point K, and placing all elements LESS than the pivot to the left of it
and all elements GREATER than the pivot to the right of it.


intuition:
use an approach that creates two windows from the beginning of the array

the key here is that our LOW pointer represents the end of the smaller_than window.
the hi pointer represents the section of the array that we're currently considering.

'''

def partition(arr, piv, lo, hi):
    if not arr:
        return
    i = lo - 1
    #this just keeps the routine easier by letting our piv stay at the end
    #then we can just swap it out at the end
    arr[piv], arr[hi] = arr[hi], arr[piv]
    for j in range(lo, hi):
        if arr[j] < arr[hi]:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]



data = [6,9,4,1,7,8]


import random

def quicksort(arr):

    def do_quicksort(arr, lo, hi):
        print(arr)
        if lo == hi:
            return
        mid = (lo + hi)//2
        piv = random.randint(lo, hi)
        #this partitioning scheme always leaves the element
        partition(arr, piv, lo, hi)
        do_quicksort(arr, mid + 1, hi)
        do_quicksort(arr, lo, mid)

    do_quicksort(arr, 0, len(arr)-1)


quicksort(data)
print(data)




















































