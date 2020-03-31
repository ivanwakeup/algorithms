'''
given a string s, return a string that contains no sequences of 3 consecutive
identical letters by removing the minimum number of consec letters.

examples:
eedaaad => eedaad, remove an 'a'
abbbcccdd => abbccdd

eeeeeee => ee

efffeee => effee


approach:
similar to longest semi alternating string. keep a count variable that
keeps track of how many times we've seen s[i] == s[i-1], don't append the current
char to the result if the count >= 2. once we see s[i] != s[i-1], reset count
'''


def string_without_3_consec(s):
    if not s or len(s) == 1:
        return s
    count = 0
    result = [s[0]]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count+=1
        else:
            count=0
        if count >= 2:
            continue
        else:
            result.append(s[i])
    return "".join(result)

datas = [
    ("eedaaad", "eedaad"),
    ("abbbcccdd", "abbccdd"),
    ("eeeee", "ee"),
    ("abcabcccdc", "abcabccdc"),
    ("eeeeeedddddffddddee", "eeddffddee"),
    ("uuuuxaaaaxuuu", "uuxaaxuu")
]

for data in datas:
    try:
        assert(string_without_3_consec(data[0]) == data[1])
        print(f"assertion succeeded for {data[0]} == {data[1]}")
    except AssertionError:
        print(f"assertion failed for for {data[0]} == {data[1]}")


