'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.




intuition:

we can use binary search BECAUSE of the following:
if we find that any given element i has a neighbor that is greater,
then we know a peak must be in the half of the array that contains its neighbor for 2 cases:
1. the neighbor itself might be the peak, if it is greater than its next neighbor
2. or perhaps the neighbor's neighbor is greater (in which case that might be the peak), all the way up to the end of the array
'''


class Solution:
    def findPeakElement(self, nums):
        if not nums or len(nums) == 1:
            return 0
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            prev = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            nxt = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')
            if prev < nums[mid] > nxt:
                return mid
            elif nums[mid] < prev:
                hi = mid - 1
            else:
                lo = mid + 1

        return "lol you'll never get here"