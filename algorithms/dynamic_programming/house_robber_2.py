'''
theres kind of a clever solution here:

1. we literally reuse the solution to house robber 1
2. the intuition here is that we can just check two cases:
    -our solution includes the first house (which means it can't include the last house)
    -our solution does NOT include the first house (Which means it DOES include the last house)

the cases here are represented by n1 and n2 respectively. so, just solve house robber 1 for each of
those cases and take the max!

'''


class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        def house_robber_1(nums):
            if not nums:
                return 0
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            for i in range(1, len(nums)):
                if i >= 2:
                    robbed = nums[i] + dp[i - 2]
                    not_robbed = dp[i - 1]
                    dp[i] = max(robbed, not_robbed)
                else:
                    dp[i] = max(nums[i], dp[i - 1])
            return dp[-1]

        n1 = nums[:-1]
        n2 = nums[1:]

        return max(house_robber_1(n1), house_robber_1(n2))