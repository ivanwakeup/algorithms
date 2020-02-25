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


class Solution  (object):
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








'''
the optimized approach has some intuitions:

we need to realize a few things. first: if the cumulative some at some index J is the SAME as it is at some previous index I, then the sum between those two elements must be 0

extend the idea to realize that if the difference of sums[i] and sums[j] is K, the sum between those elements is K.


THE MAIN INTUITION:
we really just need to keep track of two things, then:
1. what is the cumulative sum up to index i? if its k, then we found a subarray
2. have we seen the sum sum[i]-k before? if we do then we KNOW we just found a new segment of array
that contains our target


A BIG THING TO UNDERSTAND:
we keep track of the number of times we've seen a given sum. this is important. if we've seen a given sum twice, for example,
and then we see it again--we know we've got at least TWO subarrays that include the now third time we've seen that number.


further, we keep track of how many times we've seen a sum REGARDLESS of if the rolling-k is in the dict. WHY?
because this sum might later represent a rolling-k which IS in the dict which tells us we just found a window of sum K.


'''
from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        d = defaultdict(int)
        d[0] = 1
        result = 0
        rolling = 0
        for i, num in enumerate(nums):
            rolling+=num
            if rolling-k in d:
                result+= d[rolling-k]
            d[rolling] = d[rolling]+1
            print(d)
        return result


sol = Solution()
data = [3,4,7,2,-3,1,4,3,-3,3,-3,3,-3,3,-3,3]
print(sol.subarraySum(data, 7))
