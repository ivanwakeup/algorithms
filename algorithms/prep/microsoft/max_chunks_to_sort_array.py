'''
given an array of integers, find the maximum number of slices we can split the array into
such that:
after sorting each slice and then concatenating the array back together, the total array is sorted

[2,4,1,6,5,9,7] => can be split into slices [2,4,1] [6,5] [9,7], result is 3
[4,3,2,6,1] => can't be split into ANY slices, so return 1

intuition:
we are trying to find as many slices as possible such that everything in the left slice is LESS than or
equal to everything in the right slice.


plan:
create an auxillary array that stores the minimum value seen to the right of the current index i
traverse the input, once we find a value arr[i] such that its less than min_right[i], increment result by 1
'''

def max_chunks_to_sort(arr):
    min_right = [0 for _ in range(len(arr))]
    min_right[-1] = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        min_right[i] = min(min_right[i+1], arr[i])
    result = 0
    for i in range(len(arr)):
        if arr[i] <= min_right[i]:
            result+=1
    return result

datas = [
    [2,4,1,6,5,9,7],
    [4,3,2,6,1],
    [2,1,6,4,3,7],
    [0],
    [1,2,3,4,5]
]

for data in datas:
    print(
        max_chunks_to_sort(data)
    )