'''
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.
'''

'''
approach is to start with a window of size 3, keep track of the current_difference_between_elements
if the curr element - prev element is different, we move the lo pointer forward 1


approach:
create diff array where diff[i] tells us what is the abs(diff) between diff[i] and diff[i-1]

create DP array where dp[i] stores how many new arithmetic slices did dp[i] add to our result?

ex:
input = [1,2,4,6,4,3,2]
diff = [inf, 1, 2, 2, 2,1,1]
dp = [0, 0, 0, 1, 2]
'''

from typing import List

# class Solution:
#     def numberOfArithmeticSlices(self, A) -> int:
#         if not A:
#             return 0
#         diff = [0 for _ in range(len(A))]
#         diff[0] = float('inf')
#         for i in range(1, len(A)):
#             diff[i] = A[i] - A[i - 1]
#         dp = 0
#         result = 0
#         for i in range(2, len(A)):
#             if diff[i] == diff[i - 1]:
#                 dp = dp + 1
#                 result += dp
#             else:
#                 dp = 0
#
#         return result
#
# sol = Solution()

'''

[0,0,1,2,3,0,1]

dp[i] answers how many slices does the ith element add?
    -if it continues a sequence, then it adds 1 + dp[i-1]
    -if it doesn't then dp[i] = 0, unless we've seen 2 curr-prev

optimization:
we don't even need a dp array, because the current value of dp only depends on the previous value in each iteration.
'''


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:

        if len(A) < 3:
            return 0

        result = 0
        dp = 0

        prev_diff = A[1] - A[0]
        diff_cnt = 1
        for i in range(2, len(A)):
            if A[i] - A[i - 1] != prev_diff:
                diff_cnt = 1
                prev_diff = A[i] - A[i - 1]
            else:
                diff_cnt += 1
            if diff_cnt >= 2:
                dp = 1 + dp
            else:
                dp = 0

            result += dp

        return result

sol = Solution()

datas = [
    ([1,3,5,7,9], 6),
    ([3, -1, -5, -9], 3),
    ([1,2,4,6,4], 1)
]

for data in datas:
    try:
        assert(sol.numberOfArithmeticSlices(data[0]) == data[1])
        print(f"assertion passed at {data[0]} for {data[1]}")
    except AssertionError:
        print(f"assertion failed at {data[0]} for {data[1]}")
