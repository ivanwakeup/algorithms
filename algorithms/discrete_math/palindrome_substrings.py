def countSubstrings(s):
    if len(s) == 1:
        return 1
    if s == s[::-1]:
        return 1
    for i in range(len(s)):
        return countSubstrings(s[i]) + countSubstrings(s[i+1:])


print(countSubstrings("abc"))
