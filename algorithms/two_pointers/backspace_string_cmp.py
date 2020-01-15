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


'''
earlier version of backspace compare, better runtime
'''

def is_backspace(s1, s2):
    cur1 = ''
    cur2 = ''
    for char in s1:
        if char == "#":
            cur1 = cur1[:len(cur1)-1]
        else:
            cur1 += char
    for char in s2:
        if char == "#":
            cur2 = cur2[:len(cur2)-1]
        else:
            cur2 += char

    return cur1 == cur2

print(is_backspace("abab##", "ab#"))