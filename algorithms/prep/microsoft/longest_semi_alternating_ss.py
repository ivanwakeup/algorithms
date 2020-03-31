'''
given a string consisting of chars 'a' and 'b'

find the length of the longest semi-alternating substring, where "semi-alternating" means
the substring contains no sequence of chars 'a' or 'b' that appear 3 times in succession.


examples:
"baabaabaaa" => ans = 9, "baabaabaa"
"aabbabaab" => ans = 9, the entire string
"aaabbaa" => ans = 6, "aabbaa"

"abaaabbaabab" => ans = 9, "aabbaabab"
"baaabbabbb" => ans = 7, "aabbabb"

"aaa" => 2
"aa" => 2


solution:
use a sliding window, keep moving HI forward until our count_prev_same = 2,
at which point we move the lo pointer to hi-1 and continue on
'''

def longest_semi_alternating(s):
    if not s:
        return 0
    lo, hi = 0, 1
    result = 1
    count = 0
    while hi < len(s):
        if s[hi] == s[hi-1]:
            count+=1
        else:
            count = 0
        if count == 2:
            lo = hi - 1
            count = 1
        result = max(result, hi - lo + 1)
        hi+=1
    return result


datas = [
    ("baabaabaaa", 9),
    ("aabbabaab", 9),
    ("baaabbabbb", 7),
    ("aaa", 2),
    ("a", 1),
    ("aabbaabb", 8)
]

for data in datas:
    try:
        assert(longest_semi_alternating(data[0]) == data[1])
        print(f"assertion succeeded for {data[0]} == {data[1]}")
    except AssertionError:
        print(f"assertion failed for for {data[0]} == {data[1]}")

