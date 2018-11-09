def isMatch(s, p):
    sl = len(s)
    pl = len(p)

    dp = [[False for _ in range(sl + 1)] for _ in range(pl + 1)]

    dp[0][0] = True

    for i in range(1, pl + 1):
        if p[i-1] == "*" and i - 2 >= 0 and dp[i-2][0]:
            dp[i][0] = True
        else:
            dp[i][0] = False

    for i in range(1, pl + 1):
        for j in range(1, sl + 1):
            if p[i-1] != "*":
                dp[i][j] = dp[i-1][j-1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
            else:
                dp[i][j] = dp[i-2][j] or dp[i - 1][j]
                if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                    dp[i][j] |= dp[i][j - 1]

    print_matrix(dp)
    return dp[pl][sl]


def isMatchFails(s, p):
    sl = len(s)
    pl = len(p)

    dp = [[False for _ in range(pl + 1)] for _ in range(sl + 1)]

    dp[0][0] = True

    for i in range(1, pl + 1):
        if p[i - 1] == "*" and i - 2 >= 0 and dp[0][i - 2]:
            dp[0][i] = True
        else:
            dp[0][i] = False

    for i in range(1, sl + 1):
        for j in range(1, pl + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or dp[i][j-1]

    print_matrix(dp)
    return dp[sl][pl]


def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)


print(isMatch("aa", "a*"))
print(isMatchFails("aa", "a*"))