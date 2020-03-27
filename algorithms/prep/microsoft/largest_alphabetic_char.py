'''
Given a string S, find the largest alphabetic character, whose both uppercase and lowercase appear in S.
The uppercase character should be returned. For example, for S = "admeDCAB", return "D".
If there is no such character, return "NO".

largest = highest lexicographic character


plan:
create two integer arrays of 26 length, one to store uppercase chars and the other lowercase
iterate over S a
'''

def largest_alphabetic(s):
    lower = [0 for _ in range(26)]
    upper = [0 for _ in range(26)]
    for char in s:
        if ord(char) < ord('a'):
            pos = ord(char) - ord('A')
            upper[pos]+=1
        else:
            pos = ord(char) - ord('a')
            lower[pos]+=1

    for i in range(25, -1, -1):
        if upper[i] and lower[i]:
            return chr(ord('A')+i)

    return "NO"

datas = [
    "admeDCAB",
    "DDABDAFZz",
    "z",
    "aAzZzZbcCb"
]
for data in datas:
    print(
        largest_alphabetic(data)
    )