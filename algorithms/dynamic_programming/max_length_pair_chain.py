'''
two solutions:

1. dynamic programming, similar to other problems where dp[i] depends on the dp answers for every index UP to i
    so, in this case dp[i] = {
            if can_merge(pairs[i], pairs[j]), dp[i] = max(dp[i], 1+dp[j]) FOR ALL j less than i
    }

2. the solution similar to "merge intervals", in 0(nlogn) time
    - if we can chain the current interval with the previously max chained interval, do so and increment result
    - if not, we have to check if the current intervals end is LESS than the previous and update our max_chained =>
        this accounts for the cases in examples like [[-6,9], [1,8], [9,11]] where we can merge the 2nd and 3rd intervals.

[[-6,9], [1,8], [9,11]]
[[1,2], [2,3], [3,4]]

these two examples highlight the:
    elif pairs[i][1] < max_chained[1]:
                max_chained[1] = pairs[i][1]

section of code very well.

'''


class Solution:
    def findLongestChain_DP(self, pairs) -> int:

        def can_chain(p1, p2):
            return p2[0] > p1[1]

        pairs.sort(key=lambda x: x[0])

        dp = [1 for _ in range(len(pairs))]

        for i in range(1, len(pairs)):
            for j in range(0, i):
                if can_chain(pairs[j], pairs[i]):
                    dp[i] = max(dp[i], 1 + dp[j])

        return dp[-1]


class Solution:
    def findLongestChain_merge_intervals_approach(self, pairs) -> int:

        def can_chain(p1, p2):
            return p2[0] > p1[1]

        pairs.sort(key=lambda x: x[0])

        result = 1

        max_chained = [pairs[0][0], pairs[0][1]]

        for i in range(1, len(pairs)):
            if can_chain(max_chained, pairs[i]):
                result += 1
                max_chained[1] = pairs[i][1]
            elif pairs[i][1] < max_chained[1]:
                max_chained[1] = pairs[i][1]

        return result

