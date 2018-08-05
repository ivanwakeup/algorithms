def strStr(haystack, needle):
    if needle == "" or needle == haystack:
        return 0
    i = 0
    j = 0
    while i<len(haystack) and j<len(needle):
        if needle[j] == haystack[i]:
            j += 1
            i += 1
        elif j > 0:
            i = j
            j = 0
        else:
            i +=1
            j = 0

    return i - len(needle) if j == len(needle) else -1



print(strStr("mississippi", "issip"))