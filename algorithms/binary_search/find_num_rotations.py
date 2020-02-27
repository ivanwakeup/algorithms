'''
given a rotated sorted array, find the number of times the array is rotated!

ex:

arr = [8,9,10,2,5,6] ans = rotated 3 times
arr = [2,5,6,8,9,10] ans = rotated 0 times


intuition:
if the array is sorted (but rotated some number of times), we will have 1 element that is less than both of its neighbors!
using this fact, we know we've found the min when we find an element i such that i-1 > i < i + 1
so we can use the same approach as binary search to find a given target in a rotated sorted array.

'''

import logging
log = logging.getLogger()


def find_num_rotations(arr):
    lo, hi = 0, len(arr)-1
    while lo<= hi:
        mid = (lo+hi)//2
        prev,next = (mid-1)%len(arr), (mid+1)%len(arr)
        if prev > mid < next:
            return mid
        elif arr[mid] > arr[hi]:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


data = [([8,9,10,2,5,6], 3), ([2,5,6,8,9,10], 0), ([1,2], 0), ([2,3,1], 2), ([8,9,10,1,2], 3), ([3,4,1], 2)]


for arr, expected in data:
    try:
        assert find_num_rotations(arr) == expected
    except AssertionError:
        log.error((f"{arr} did not return expected result of {expected}"))
        raise
