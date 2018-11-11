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
    print('\n'.join(table))


# print(isMatch("aa", "a*"))
# print(isMatchFails("aa", "a*"))


'''
recurrence:
DP(i, j) = string from position I onwards matches pattern from position j onwards
BASE CASE:
if you have no pattern left, then the only match is if you have no string left
if next character is a star, two possibilities:
1. the current characters match AND the rest of the string matches the pattern
2. the current characters dont match and the current string matches the pattern excluding p[i] and p[i+1] 
= max {
    DP(i+1, j+1) if s[i] == p[j]
    
}
'''
def naive_regex_matcher(s, p):

    if not p:
        return not s

    if not s:
        matches = False
    else:
        matches = (s[0] == p[0] or p[0] == '.')

    if len(p) >= 2 and p[1] == "*":
        cur_match = matches and naive_regex_matcher(s[1:], p)
        cur_dont_match = naive_regex_matcher(s, p[2:])
        result = max(cur_match, cur_dont_match)
    else:
        result = naive_regex_matcher(s[1:], p[1:])

    return result

print(naive_regex_matcher("a*", "aa"))



class Solution(object):
    def isMatch(self, s, p):
        sl = len(s)
        pl = len(p)

        dp = [[False for _ in range(sl + 1)] for _ in range(pl + 1)]

        dp[0][0] = True

        for i in range(1, pl + 1):
            if p[i-1] == "*" and dp[i-2][0]:
                dp[i][0] = True

        for i in range(1, pl + 1):
            for j in range(1, sl + 1):
                if p[i-1] != "*":
                    #no star, previous pattern and string match AND current string and pattern match
                    dp[i][j] = dp[i-1][j-1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    #is star, either pattern matches WITHOUT star and previous or the previous regex character matched the current
                    dp[i][j] = dp[i-2][j] or dp[i - 1][j]
                    #if we have a star and the previous part of the regex matched the current string, we STILL have a match
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        dp[i][j] |= dp[i][j - 1]

        return dp[pl][sl]