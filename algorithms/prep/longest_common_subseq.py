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


def longest_common_subsequence(word1, word2):
