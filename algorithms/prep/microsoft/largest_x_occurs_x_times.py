'''
given an array of integers of length N, find the largest integer X that occurs exactly X times

ex:
[2,8,1,3,2,3,3,4] => return 3, it occurs 3 times
[4,4,3,2] => return 0, no number appears as many times as itself
[5,5,5,5,5] => return 5

plan:
keep a hashmap of how mu
'''

from collections import defaultdict
def largest_x_occurs(nums):
    hm = defaultdict(int)
    result = 0
    for num in nums:
        hm[num]+=1
        if hm[num] == num:
            result = max(num, result)
    return result

print(
largest_x_occurs([2,8,1,3,2,3,3,4])
)

