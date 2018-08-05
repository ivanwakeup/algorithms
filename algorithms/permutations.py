def permute(s):

    out = []

    if len(s) == 1:
        out.append(s)

    for idx, letter in enumerate(s):
        for perm in permute(s[:idx] + s[idx+1:]):
            out.append(letter + perm)

    return out



print(permute("this"))
