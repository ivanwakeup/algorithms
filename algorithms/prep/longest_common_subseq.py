'''
step1 - define the subproblems:

let i = len(s1)
let j = len(s2)

if s1[i] and s2[j] match, then LCS = 1 + LCS of rest

LCS(s1, s2) = max( 1 + LCS(s1[:i], s2[:j]), LCS(s1[:i], s2[:j+1]), LCS(s1[:i+1], s2[:j]) )
= max of 1 + LCS(restofs1, restofs2) if match, or LCS including Ith char or Jth char
'''


word1 = "HIEROGLYPHOLOGY"
word2 = "MICHAELANGELO"

#base cases? length of word1 or word2 is 1 or 0


def top_down_longest_common_subsequence(word1, word2, memo):

    key = word1 + ":" + word2
    if key in memo:
        return memo[key]

    if not word1 or not word2:
        return 0

    if word1[0] == word2[0]:
        result = 1 + top_down_longest_common_subsequence(word1[1:], word2[1:], memo)
    else:
        result = max(top_down_longest_common_subsequence(word1, word2[1:], memo), top_down_longest_common_subsequence(word1[1:], word2, memo))

    memo[key] = result
    return result


print(top_down_longest_common_subsequence(word1, word2, {}))


'''what is the runtime of the top-down memoized version? best case O(n), worst case O(n^2) because you have to solve LCS twice for each.
Without memoization, it's 2^n runtime, because you have to sovle 
'''

def bottom_up_lcs(word1, word2):

    m = len(word1)
    n = len(word2)

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


#print(bottom_up_lcs(word1, word2))


'''
you could save even more space on LCS by only storing the 3 previous values you care about in the DP array:
dp[i-1][j-1]
dp[i][j-1]
dp[i-1][j]
'''