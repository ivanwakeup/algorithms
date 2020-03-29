'''
given a string consisting of the characters 'A' and 'B',
return the minimum number of deletions of either A or B deleted
to partition the string such that all the As are on the left and all the Bs are on the right

examples
"BAAABAB", ans = 2, we could delete the first and second to last B
"ABAB", ans = 1, we could delete the first B or the second A
"BBABAA", ans = 3, we have to delete ALL the Bs or ALL the As
"BAABBAB", ans = 2, we could delete the first and second to last B

observations:
1. we aren't "swapping" characters, only deleting them
2. seems like a dynamic programming problem



if the ith character is different than the i-1th character, we need an additional delete.
AB -> 0 delete
ABA -> 1 delete
ABAA -> 1 delete
ABAB -> 1 deletes

BABAAABBA -> 3 delete
ABBA -> 1 delete

BBBAAA->

every time you encounter a "BA", you could imagine removing that sequence from the string
keep doing so until you have no more "BA" sequences?

'''

def min_deletions(s):
    stack = []
    result = 0
    for char in s:
        if char == "A" and stack and stack[-1] == "B":
            stack.pop()
            result+=1
            continue
        else:
            stack.append(char)
    return result


datas = [
    ("BBAAABA", 3),
    ("BAAABAB", 2),
    ("BBBAAA", 3),
    ("ABBBBBA", 1),
    ("AAAA", 0),
    ("BBBBB", 0),
    ("ABABAB", 2)
]

for data in datas:
    try:
        assert(min_deletions(data[0]) == data[1])
        print(f"assertion passed at {data[0]} for {data[1]}")
    except AssertionError:
        print(f"assertion failed at {data[0]} for {data[1]}")