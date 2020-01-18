'''

given an array that is K-sorted, such that any elements are almost sorted and no further than K elements away from their intended
sorted order, find an efficient way to sort the array.

ex:
[1,4,5,2,3,7,8,6,10,9], k = 2


intuition:
because we have the K factor, we can use a min heap and only add up to k+1 elements to it
we effectively consider windows of size k+1 that move along the array
the position that we're "filling" is the first position in the window, we pop off the min heap

and then we add the next element in the array to be considered.


plan:
keep pointer i to current position to be inserted
iterate over array
    once we added k index, pop off min heap
    insert popped value into i
    move i forward

while heap:
    update arr[i]
    move i forward
'''

import heapq
def sort_k_sorted_array(arr, k):
    i = 0
    heap = []
    for idx, num in enumerate(arr):
        if idx > k:
            item = heapq.heappop(heap)
            arr[i] = item
            i+=1
        heapq.heappush(heap, num)

    while heap:
        item = heapq.heappop(heap)
        arr[i] = item
        i+=1


data = [1,4,5,2,3,7,8,6,10,9]
sort_k_sorted_array(data, 2)
print(data)