def backspaceCompare(S, T):
    p1 = len(S) - 1
    p2 = len(T) - 1
    s1 = 0
    s2 = 0

    while p1 >= 0 and p2 >= 0:
        # do algo
        while p1 >= 0 and (S[p1] == "#" or s1):
            if S[p1] == "#":
                s1 += 1
            elif s1:
                s1 -= 1
            p1 -= 1
        while p2 >= 0 and (T[p2] == "#" or s2):
            if T[p2] == "#":
                s2 += 1
            elif s2:
                s2 -= 1
            p2 -= 1
        # now compare
        if p1 >= 0 and p2 >= 0:
            if S[p1] != T[p2]:
                return False
        p1 -= 1
        p2 -= 1

    # handle S has chars left
    while p1 >= 0:
        if S[p1] != "#":
            if not s1:
                return False
            s1 -= 1
        else:
            s1 += 1
        p1 -= 1

    # handle T has chars left
    while p2 >= 0:
        if T[p2] != "#":
            if not s2:
                return False
            s2 -= 1
        else:
            s2 += 1
        p2 -= 1

    return p1 < 0 and p2 < 0


print(backspaceCompare("bxj##tw", "bxj###tw"))