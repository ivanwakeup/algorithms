'''
Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome.
If not possible, return -1.

Example 1:

Input: "mamad"
Output: 3
Example 2:

Input: "asflkj"
Output: -1
Example 3:

Input: "aabb"
Output: 2
Example 4:

Input: "ntiin"
Output: 1
Explanation: swap 't' with 'i' => "nitin"



approach:
first check if we can form a palindrome with the given string
if so, start with two pointers at the outsides of the string. if we don't have to move those, we definitely
don't need to consider them in the swapping so we can move our pointers inwards

once we find a s[lo] != s[hi], we know we need to make a swap.
the minimum number of swaps we could do would be to just find an index K that is less than HI
but greater than LO that we can swap HI with. once we do, we can move on.

'''
from algorithms.utils import assert_test_cases


def min_swaps_palindrome(s):

    def can_make(s):
        counts = [0 for _ in range(26)]
        for char in s:
            counts[ord(char)-ord('a')]+=1
        odd_cnt = 0
        for item in counts:
            if item % 2:
                odd_cnt+=1
        return odd_cnt <= 1

    def swap_chars(s, i, j):
        arr = list(s)
        arr[i], arr[j] = arr[j], arr[i]
        return "".join(arr)

    if not can_make(s):
        return -1
    lo, hi = 0, len(s) - 1
    result = 0
    while lo<hi:
        if s[lo] == s[hi]:
            lo+=1
            hi-=1
            continue
        k = hi - 1
        while k > lo and s[k] != s[lo]:
            k-=1
        if k == lo:
            s = swap_chars(s, k, k+1)
            result+=1
            continue
        while k < hi:
            s = swap_chars(s, k, k+1)
            result+=1
            k+=1
        lo+=1
        hi-=1

    return result


datas = [
    ("mamad", 3),
    ("damam", 3),
    ("asflkj", -1)
]

assert_test_cases(datas, min_swaps_palindrome)