def longest(s):
    length = len(s)
    ans = 0
    hash = dict()

    i = 0

    for j in range(0, length):
        if s[j] in hash:
            i = max(hash.get(s[j]), i)
        ans = max(ans, j - i + 1)
        hash[s[j]] = j + 1

    return ans

print(longest("hellohello"))
