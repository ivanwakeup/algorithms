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


'''
here's an incorrect solution. this solution assumes that dp[i] stores the BEST LIS we could make up
to that point.
unfortunately, we can't do this. instead, what dp[i] must answer is "if we DO include this element, whats the best LIS"?

to see the difference, check out this example:

[4,10,4,9] -> if we use the erroneous approach, our dp array would look like: [1,2,2,3], which gives the wrong result
      ^
      
when we are considering idx 3, the best LIS we can make by including it is length 1 => [4,10,4]. so our dp[i] SHOULD
look like: [1,2,1]

and then when we add 9 -> [4,10,4,9]
dp = [1,2,1,2]

see the correct example below for how this has to be handled.
'''

class Solution_incorrect(object):
    def lengthOfLIS(self, nums):

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-1]

        return dp[-1]



'''
correct solution that doesn't "carry forward" dp[i-1], but instead marks dp[i] as the "best we can do by ADDING the i'th element"
'''
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



