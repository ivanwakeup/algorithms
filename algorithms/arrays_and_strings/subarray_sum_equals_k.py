'''

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


intuitions:
keeping a prefix sum array allows us to ask, is the sum between some indexes i and j equal to our target sum of k?

with this approach, we still need to check all n^2 subarrays, but when we ask what is the sum between them we get a constant
time answer if we pre compute the array's prefix sum
'''


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        ps = self.prefix_sum(nums)
        print(ps)
        for i in range(len(nums)):
            for j in range(i, len(nums)+1):
                if ps[j] - ps[i] == k:
                    print(nums[i:j])
                    res+=1
        return res

    def prefix_sum(self, arr):
        if not arr:
            return arr
        res = [0]
        for i in range(1, len(arr)+1):
            res.append(res[i-1] + arr[i-1])
        return res



sol = Solution()
data = [3,4,7,2,-3,1,7,2]
print(sol.subarraySum(data, 7))