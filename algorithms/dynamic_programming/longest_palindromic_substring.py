'''

INTUITION:
The brute force approach simply checks all n^2 substrings and if they are a palindrome in 0(n) time for n^3 time

we optimize by realizing that we repeat work when we check if substrings are palindromes. if we're checking length 3 substrings
at  lps(s, i, j), and we know that lps(s, i+1,j-1) is a palindrome, we don't need to check if the whole thing is a palindrome
again

by memoizing whether s[i:j] is palindromic, we reduce our runtime by O(n)
'''
class Solution:
    def longestPalindrome(self, s):
        dp = [[0] * len(s) for i in range(len(s))]
        ans = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if ans == "" or max_length < j - i + 1:
                        ans = s[i:j+1]
                        max_length = j - i + 1
        return ans



sol = Solution()

print(
    sol.longestPalindrome("abadffffa")
)