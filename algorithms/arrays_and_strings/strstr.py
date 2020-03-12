class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        for i in range(len(haystack)):
            j = 0
            prev = i
            while haystack[i] == needle[j]:
                i+=1
                j+=1
                if j == len(needle):
                    return prev
        return res

sol = Solution()

print(
    sol.strStr("mississippi", "issip"),
    sol.strStr("hello", "ll"),
    sol.strStr("aaaaa", "bba")
)