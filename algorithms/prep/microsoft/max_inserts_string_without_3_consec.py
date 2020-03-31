'''
given a string S of length N,
return the maximum number of 'a's that can be inserted into the string
without winding up with 3 consecutive 'a's, including the end and beginning of the string.

if the string already contains 'aaa', return -1.

example:
dog => aadaaoaagaa, ans = 8 a's
aabca => aabaacaa, ans = 3 a's
baabaa => aabaabaa, ans = 2 a's
cadaba => aacaadaabaa, ans = 5 a's
a => aa, ans = 1 a's
ba => aabaa, ans = 3 a's
aa => aa, ans = 0 a's


solution:
keep track of how many a's we've seen between the current char and the next non-'a' char we encounter

'''

def max_inserts_string_3_chars(s):
    result = 0
    count = 0
    for char in s:
        if char == 'a':
            count+=1
            if count == 3:
                return -1
        else:
            result += 2 - count
            count = 0

    result += 2-count
    return result

datas = [
    ("dog", 8),
    ("aabca", 3),
    ("a", 1),
    ("aa", 0),
    ("baabaa", 2),
    ("ba", 3)
]

for data in datas:
    try:
        assert(max_inserts_string_3_chars(data[0]) == data[1])
        print(f"assertion succeeded for {data[0]} == {data[1]}")
    except AssertionError:
        print(f"assertion failed for for {data[0]} == {data[1]}")