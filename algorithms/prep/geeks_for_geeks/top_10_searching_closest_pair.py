'''
Given a sorted array and a number x, find a pair in array whose sum is closest to x.
Examples:

Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10

'''

'''
examples:

arr = [1,2,3,4] sum = 4
ans = [1,4]

arr = [1, 21, 30, 30, 31, 35, 61] sum = 62
ans = [30,31]

arr = [1,40,41,61] sum = 81
ans = [40,41]

can input be negative?
no

what if more than 1 ans?
return any ans

observations:
if found a pair that == x, return that pair
otherwise we will need to look at the whole array?


could just look at every pair in the array, and keep track of the pair and their distance from x, updating the minimum distance along the way

the array is sorted, so could also start from each end and just iterate inwards?

approach:
start at each end
min_pair = (i, j, diff)
while i < j:
    update min_pair
    if arr[j] + arr[i] > sum:
        move j inwards
    else:
        move i inwards
return min_pair

cold we do this with binary search?
1. could try to find a value that is half the sum and start from there?
'''


# Input: arr[] = {1, 3, 4, 7, 10}, x = 15
# Output: 4 and 10


def find_min_pair(arr, target_sum):
    if not arr:
        return (None, None)
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return (arr[0], arr[1])

    i=0
    j=len(arr)-1
    min_diff = float('inf')
    min_pair = (arr[i], arr[j])
    while i < j:
        cur_diff = abs(target_sum - (arr[j]+arr[i]))
        if cur_diff < min_diff:
            min_diff = cur_diff
            min_pair = (arr[i], arr[j])
        if arr[j] + arr[i] == target_sum:
            return min_pair
        elif arr[j] + arr[i] > target_sum:
            j-=1
        else:
            i+=1
    return min_pair


print(find_min_pair([10, 22, 28, 29, 30, 40], 54))



