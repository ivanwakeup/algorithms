from typing import List
from algorithms.utils import assert_test_cases

'''
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
'''

'''
it is subtle, but this first solution is incorrect. accumulating the result like:
result += do_find(coins, amount - coin, memo)
does not answer how many unique ways are there to produce the given AMOUNT with COINS.

this is because we need to keep track of answer_sets we've already made.
'''
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#
#         def do_find(coins, amount, memo):
#             if amount == 0:
#                 return 1
#             if amount in memo:
#                 return memo[amount]
#             result = 0
#             for coin in coins:
#                 if amount - coin >= 0:
#                     result += do_find(coins, amount - coin, memo)
#             memo[amount] = result
#             return result
#
#         memo = {}
#         return do_find(coins, amount, memo)


'''
this is the correct solution, and a bit more intuitive.

intuition:
our DP[i] answers: how many ways could we make the i'th amount by using all the coins up to and including
the current coin we're considering?

as we iterate over dp on the FIRST coin, we're calculating how many ways we could make each amount using
only the first coin.

when we iterate the NEXT time, dp[i] = dp[i-coin] + dp[i] tells us how many ways could we make the dp[i-coin]
amount PLUS how many ways to make the dp[i] amount given the coins we've considered so far?

'''
class Solution(object):
    def change(self, amount, coins):
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(1, len(dp)):
                if i - coin >= 0:
                    dp[i] = dp[i-coin] + dp[i]
        return dp[-1]

sol = Solution(
)

datas = [
    (5, [1,2,5], 4)
]

assert_test_cases(datas, sol.change)