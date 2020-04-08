'''

intuitions:
dp(i, j) answers what is the answer between indexes i and j?

the answer is simply the max leaf value we found in [i...k] * max leaf value we found in [k+1....n]
these values represent what will ultimately be the final root node value, so we obviously include that in the result

and then we add the result of dp(i, k) + dp(k+1, j) <= these results represent the best we could
do for each subtree, and of course we have to consider all possible partitionings of the input

ex:

[6,2,2,3] <= the middle partition [2,2] forms the best answer with 6 and 3 on either side of the tree respectively.
'''


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        memo = {}

        def do_find(i, j):
            key = str(i) + ":" + str(j)
            if key in memo:
                return memo[key]
            if i >= j:
                return 0
            result = float('inf')
            for k in range(i + 1, j + 1):
                result = min(
                    result,
                    (max(arr[i:k]) * max(arr[k:j + 1])) + do_find(i, k - 1) + do_find(k, j)
                )
            memo[key] = result
            return result

        return do_find(0, len(arr) - 1)

