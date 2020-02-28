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

INTUITION for the correct solution:

at any given index nums[i], we want to answer:
CAN i make a longer increasing subseq by including this element?

to answer this question, we can't just consider the i-1th element, because the i-1th element might NOT be part
of the LIS

DP[I] DOES NOT DENOTE THE "BEST YOU CAN DO AT i". it denotes "THE BEST YOU CAN DO IFF YOU TRY AND EXTEND the LIS by including
this element".

With that in mind, we can see why we would need to check every index i that is less than our current index j and apply the same
logic. the answer for dp[i] does not lie just at dp[i-1], because, again, we need to know "what is the best i can do by INCLUDING
this current element"

so, we have to check EVERY i less than j and answer, is my nums[i] > nums[j]? if so, i can make a LIS that is at least 1 longer.
this is what we store in dp[i].

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


'''
recursive formulation:

lis(nums, i) = 1 + lis(nums, i-1) if nums[i] > nums[i-1] else lis(nums, i-1)
'''

