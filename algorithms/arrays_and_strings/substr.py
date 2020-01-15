def has_sub(s, check):
    c_idx = 0
    for s_idx in range(len(s)):
        if check[c_idx] == s[s_idx]:
            if c_idx == len(check) - 1:
                return True
            c_idx += 1
        else:
            c_idx = 0
    return False




print(has_sub("this", "th"))
print(has_sub("whatawhat", "waa"))
print(has_sub("aaa", "aa"))