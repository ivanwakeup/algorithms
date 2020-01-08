def checkInclusion(s1, s2):
    chk = build_dict(s1)
    i = 0
    j = 0
    while j < len(s2):
        if s2[j] not in chk:
            while i < j:
                chk[s2[i]] += 1
                i += 1
            i = j + 1
        else:
            chk[s2[j]] -= 1
            if not chk[s2[j]]:
                del chk[s2[j]]
                if not chk:
                    return True
        j += 1
    return False


def build_dict(s):
    from collections import defaultdict
    d = defaultdict(int)
    for char in s:
        d[char] += 1
    return d

print(checkInclusion("adc", "dcda"))