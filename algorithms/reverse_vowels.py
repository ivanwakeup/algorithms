def reverseVowels(s):
    vowel = {'a', 'e', 'i', 'o', 'u'}
    strArr = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        while i < len(s) and s[i] not in vowel:
            i += 1
        while j >= 0 and s[j] not in vowel:
            j -= 1
        if i < len(s) and j >= 0:
            strArr[i], strArr[j] = strArr[j], strArr[i]
        i += 1
        j -= 1
    return "".join(strArr)

print(reverseVowels("leetcode"))