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

print(is_backspace("ab##", "aa#b"))