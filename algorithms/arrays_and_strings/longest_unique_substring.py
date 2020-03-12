def lengthOfLongestUniqueSubstring(s):
    ans = 0
    length = len(s)

    for i in range(0, length):
        for k in range(i+1, length+1):
            if allUnique(s, i, k):
                ans = max(ans, k -i)
    return ans


def allUnique(str, start, stop):
    tmp = set()
    for i in range(start, stop):
        if str[i] in tmp:
            return False
        tmp.add(str[i])
    return True



#print(lengthOfLongestUniqueSubstring("dvdz"))



#you can take the end idx subtract the start idx of a string to find its length, this is used here to determine what the actual length of the substr is

#if there are pieces of the algorithm you can split out, do it!





'''
keep counter dict
then we can just use a for loop as the fast pointer, and a int variable as the slow pointer
at the start of every loop, we check the condition "have we seen s[j] already? if so we need to move i forward and delete
chars while we do, until we remove the char we've now already seen".

the result is just the length of the window j-i+1
'''
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()
        res = 0
        i = 0
        for j in range(len(s)):
            while c[s[j]] and i < j:
                c[s[i]]-=1
                i+=1
            c[s[j]]+=1
            res = max(res, j-i+1)
        return res

sol = Solution()

print(
    sol.lengthOfLongestSubstring("pwwkew")
)




























