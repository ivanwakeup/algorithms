'''
the edit distance between two words is how many edits it takes to make w1 == w2
available edits:
1. delete a character
2. insert a character
3. replace a character

STEPS
1. define subproblem
ED(w1, w2) = min {
    if w1[i] == w2[j], then just ED(w1[i+1:], w2[j+1:])
    else:
    1 + min(ED(w[i+1:], w2), ED(w1, w2[j+1:])

}

AAAA
BAAA
'''

def brute_force_ed(w1, w2):
    if not w1:
        return len(w2)

    return do_brute_force_ed(w1, 0, w2, 0)

def do_brute_force_ed(w1, i, w2, j):

    if i == len(w1) or j == len(w2):
        return len(w2) - j if i == len(w1) else len(w1) - i

    if w1[i] == w2[j]:
        ed = do_brute_force_ed(w1, i + 1, w2, j + 1)
    else:
        ed = 1 + min(do_brute_force_ed(w1, i+1, w2, j+1), do_brute_force_ed(w1, i + 1, w2, j), do_brute_force_ed(w1, i, w2, j + 1))
    return ed


# print(brute_force_ed("CABABAGDDAH", "AAHDANHDAKLJAH"))
#
# assert(brute_force_ed("AAAA", "AAAA") == 0)
# assert(brute_force_ed("AAAA", "BBBB") == 4)
# assert(brute_force_ed("ABAB", "BBBB") == 2)
# assert(brute_force_ed("", "") == 0)
# assert(brute_force_ed("", "ABEIQ") == 5)
# assert(brute_force_ed("CABAB", "AACABABA") == 3)



def top_down_ed_memo(w1, w2):
    if not w1:
        return len(w2)

    return do_top_down_ed_memo(w1, 0, w2, 0, {})


def do_top_down_ed_memo(w1, i, w2, j, memo):

    key = w1[i:] + w2[j:]

    if key in memo:
        return memo[key]

    if i == len(w1) or j == len(w2):
        return len(w2) - j if i == len(w1) else len(w1) - i

    if w1[i] == w2[j]:
        ed = do_top_down_ed_memo(w1, i + 1, w2, j + 1, memo)
    else:
        ed = 1 + min(do_top_down_ed_memo(w1, i+1, w2, j+1, memo), do_top_down_ed_memo(w1, i + 1, w2, j, memo), do_top_down_ed_memo(w1, i, w2, j + 1, memo))

    memo[key] = ed
    return ed


print(top_down_ed_memo("SADHOOASDHNOAJDHASDOHJASDHSAJASDJASD", "ASDHIOJASDHINASDHINASDHASASDHASDJASDJSDAJASDJSADDAFSDFAsd"))