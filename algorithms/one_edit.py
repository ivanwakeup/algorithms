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


print(is_one("this", "thata"))
print(is_one("this", "thata"))
