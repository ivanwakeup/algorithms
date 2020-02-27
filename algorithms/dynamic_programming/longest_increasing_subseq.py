'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''



# class Solution(object):
#     def lengthOfLIS(self, nums):
#
#         dp = [1] * len(nums)
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i-1]:
#                 dp[i] = dp[i-1] + 1
#             else:
#                 dp[i] = dp[i-1]
#
#         return dp[-1]
#
#
# sol = Solution()
# print(
#     sol.lengthOfLIS([10,22,9,33,21,50,41,60,80])
# )

class Solution(object):
    def lengthOfLIS(self, nums):

        dp = [1] * len(nums)
        result = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
                    result = max(dp[i], result)
        return result


sol = Solution()
print(
    sol.lengthOfLIS([4,10,4,3,8,9])
)



