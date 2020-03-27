'''
given a string containing the characters only 'a' and 'b',

determine the minimum number of moves to swap a/b or b/a to obtain
a result string such that the string contains no sequences of 3 consecutive characters

ex: aa => 0
    aaa => 1
    baa => 0
    aba => 0
    aaaa => 1
    aaaaa => 1
    aabaaabaaa => 2
    bbbaaab => 2


intuition:
we need to find sequences of at least 3 characters that are the same, up to 5 characters because we know that:
aaa => 1 swap needed
aaaa => 1 swap needed
aaaaa => 1 swap needed
aaaaaa => 6 chars, so 2 swaps needed

in other words, the number of swaps we need is:
len(run_length)//3, where run_length is the length of the current consecutive string we've found
'''


def get_min_moves(s):
    result = 0
    run_length = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            run_length+=1
        else:
            result += run_length // 3
            run_length=1
    result+=run_length//3
    return result

print(get_min_moves("abbbbbbb"))
