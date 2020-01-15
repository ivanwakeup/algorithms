def is_one_edit(word1, word2):
    if abs(len(word1) - len(word2)) > 1:
        return False

    else:
        i, j = 0, 0
        diff = 0
        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                diff += 1
                if len(word1) > len(word2):
                    i += 1
                elif len(word2) > len(word1):
                    j += 1
            else:
                i += 1
                j += 1
        if len(word1) > i or len(word2) > j:
            diff += 1
        return diff == 1


print(is_one_edit("this", "athis"))



'''
alternative
'''

def is_one(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    if abs(len1 - len2) > 1:
        return False

    diffs = 0

    i = 0
    j = 0

    while i < len1 and j < len2:
        if s1[i] != s2[j]:
            if diffs == 1:
                return False

            if len1 > len2:
                i += 1

            elif len1 < len2:
                j += 1

            else:
                j += 1
                i += 1
            diffs += 1

        else:
            j += 1
            i += 1

    if i < len1 or j < len2:
        diffs += 1

    return diffs == 1


