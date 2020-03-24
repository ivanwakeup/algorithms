'''
for understanding the runtime here (memoized), just think about the case of the outside chars
never matching.

if they dont match, we'll always make TWO calls at the current level of the recursive tree. This would seem
to suggest the runtime is 0(2^n), but the memoization ensures we never solve a subproblem that's been solved.

so, how many DISTINCT subproblems are there? well there are only n^2! lps(s, i, j) tells us the answer
between s[i:j], and there are only n^2 distinct slices of the array we can make.
'''


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}
        return self.lps(s, 0, len(s) - 1, memo)

    def lps(self, s, i, j, memo):
        key = str(i) + ":" + str(j)
        if key in memo:
            return memo[key]
        if i > j:
            return 0
        if i == j:
            return 1
        result = 0
        if s[i] == s[j]:
            result = 2 + self.lps(s, i + 1, j - 1, memo)
        else:
            result = max(self.lps(s, i + 1, j, memo), self.lps(s, i, j - 1, memo))
        memo[key] = result
        return result




'''
matrix approach intuition:
1. matrix[i][j] answers: what is the LPS of s[i:j]?
2. we fill out the matrix "diagonally", as this corresponds to considering substrings of length K
    as we complete the matrix
    -we can calculate the slice from i to j by j = i + K - 1
    -on each inner loop of i, only iterate until i-k + 1 (so j doesn't go out of bounds)

3. the COLUMNS in the matrix correspond to J, or the end of the substring we're considering for LPS
    the ROWS in the matrix correspond to I, or the beginning of the substring we're considering for LPS

'''


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s) - 1):
            dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1

        for k in range(3, len(s) + 1):
            for i in range(len(s) - k + 1):
                j = i + k - 1
                dp[i][j] = 2 + dp[i + 1][j - 1] if s[i] == s[j] else max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(s) - 1]

