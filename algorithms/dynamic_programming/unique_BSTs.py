from algorithms.utils import assert_test_cases

'''
find the number of unique possible BSTs given N, using the nodes 1 to N.


main intuition:
use dp[i] to keep track of how many trees you can form with i nodes.
for the i+1th node, we need to consider each node 1....i+1 as the "top" of the binary tree

when we do, our answer while considering the jth node in range(1, i+1th) node as the top,
our answer is simply:
num_ways_to_form_tree_left * num_ways_to_form_tree_right, as denoted by dp[i]+= dp[j-1] * dp[i-j]
'''
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            for j in range(1, i + 1):
                dp[i]+= dp[j-1] * dp[i-j]

        return dp[-1]

sol = Solution()

datas = [
    (6, 132),
    (4, 14),
    (5, 42),

]

assert_test_cases(datas, sol.numTrees)