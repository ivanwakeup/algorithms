'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.


Example 2:

Input:
nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.



INTUITION:
an easy solution is to create a prefix sum from both the left and the right
then if we just iterate through the input, and we find an index such that its prefix_sum(from_left) == prefix_sum(from_right),
we've found an answer

this uses O(n) space to store the prefix sum array

OPTIMIZATION:
we don't actually need to store the full prefix sum arrays
we can use a few observations to realize that:
    1. if we first precompute the TOTAL sum of the input array, as we traverse we can just subtract the current
       element from the total sum. this running sum now serves as the "rolling sum" from the right

    2. as we iterate, we can also just add the current index to a LEFT_SUM variable, which gives us the rolling
       sum from the left side!
'''


'''
non optimized, two-array prefix sum approach
'''
class Solution:
    def pivotIndex(self, nums):
        if not nums:
            return -1
        rl = [0 for _ in range(len(nums) + 1)]
        rr = [0 for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            rl[i] = rl[i - 1] + nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            rr[i] = rr[i + 1] + nums[i + 1]

        for i in range(0, len(nums)):
            if rl[i] == rr[i]:
                return i
        return -1



'''
optimized constant space linear time approach.

this is where we use the idea of just a single variable to store the current right_sum and left_sum


you can sort of imagine a "slider" that moves across the array, and as it does, it reduces the size of the right_side array (and therby the right_sum)
and increases the size of the left_side_array, and also the left_sum

'''

class Solution:
    def pivotIndex(self, nums):
        right_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum -= nums[i]
            if right_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1
