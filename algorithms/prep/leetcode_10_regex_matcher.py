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

'''
OLD ATTEMPT!
'''
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
recursive regex matcher implementation:

rules for matching:
* - matches character preceeding 0 or more times
. - matches any character
char - matches literal character

examples:

a*
aaa
MATCHES

a*b*cc*
c
MATCHES

rules: if . or char[i] = pattern[i], match

if str[i] != pattern[i] and pattern[i] != *, no match

else if pattern is *

str

IF A STAR IS PRESENT IN THE P[1], YOU CAN EITHER PRETEND P[0:2] DOESN'T EXIST, OR YOU CAN DELETE THE CHARACTER S[0] AND CHECK THE REST OF THE STRING
WHY IS THIS?

CASES TO COVER:

IF S[I] AND P[I] MATCH AND THERE IS NO STAR IN P[1], THEN JUST SEE IF S[I+1] AND P[I+1] MATCH
IF STAR EXISTS:
THEN MAX {
    S[I] == P[I] AND MATCHES(S[I+1], P)
    MATCHES(S, P[2:])
}
'''

def naive_matcher(s, p):

    if not p:
        return not s

    matches = s and (s[0] == p[0] or p[0] == ".")

    if len(p) >= 2 and p[1] == "*":
        #two cases if there is a * coming up. either the s[i] matches pattern[i] and
        return (matches and naive_matcher(s[1:], p)) or naive_matcher(s, p[2:])
    else:
        return matches and naive_matcher(s[1:], p[1:])



print(naive_matcher("adgahdahaadasgahdagdsveagrabsdbasdbadghasbhdsbasdgadss", "a*.bc*c*b*asdg*.a*a*b*c*......g*aadjadfm"))




def naive_matcher_memoized(s, p, memo):

    key = s + ":" + p
    if key in memo:
        return memo[key]

    if not p:
        return not s

    if not s:
        matches_here = False
    else:
        #there is at least 1 char in string and pattern
        matches_here = (s[0] == p[0] or p[0] == ".")

    #if there is an upcoming *, either the s and the rest of the pattern without the star match
    #or the rest of the string and theres a match on the current char AND the rest of the string matches
    #the rest of the pattern
    if len(p) >= 2 and p[1] == "*":
        matches_without = naive_matcher_memoized(s, p[2:], memo)
        matches_with = (matches_here and naive_matcher_memoized(s[1:], p, memo))
        result = max(matches_without, matches_with)
    else:
        #if there is no upcoming *, the current chars have to match and the rest of the string and pattern have to match
        result = matches_here and naive_matcher_memoized(s[1:], p[1:], memo)
    memo[key] = result

    return result

print(naive_matcher_memoized("aabc", "a*.c*", {}))

'''
dp[i][j] = does s up to I match pattern up to J?
'''
def bottom_up_matcher(s, p):
    pass







































