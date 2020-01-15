def largeGroupPositions(s):
    result = []
    j = 0
    s+= '9'
    for i in range(1, len(s)):
        if s[i] == s[j]:
            continue
        else:
            if i - j > 2:
                result.append([j, i - 1])
            j = i
    return result



print(largeGroupPositions("aaabbccxxxxccc"))