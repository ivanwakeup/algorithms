'''
given a string containing "R" and "W", where they represent red and white balls respectively

return the minimum number of swaps needed to group all the red balls and white balls together.
swaps can be performed only with adjacent elements

ex:
"RWWWWR" -> 4 swaps needed, move the Rs in towards each other
"WRRWWR" -> 2 swaps needed, move the last R towards the two middle Rs
"RWRWRWR" -> 4 swaps

RWRWRWR
WRRWRWR
WRRWRRW
WRRRWRW
WRRRRWW


intuition:
1. we are effectively trying to "mash" the Rs together by moving outward Rs inwards towards each other
2. for a string like WRWWWRWWWR, it's clear the minimum number of swaps is 6, we need to move the outermost
Rs inwards one step at a time
3. consider what happens then with a case like WRWRWWRWWWR. its the same approach as moving the outside
Rs inwards, but the fact that the leftmost R in this string has 1 R in between it and the "center" R just
reduces the number of swaps we need by 1--because there's 1 R closer inwards than it to make up the "chunk" of Rs
in the middle.

plan:
get MID index of array containing only Rs, this is the R we want to move all other R's towards
the total of swaps needed for moving the current R (s[i]) towards the MID r index is:
(the number of swaps needed to move R towards the middle R) - (num Rs in between that R and the mid R)

the idxs array helps us answer how many Rs are there between the R we're moving toward the mid and the mid R,



what is the length between the mid R and the R we're moving inwards? => (idxs[mid] - idxs[i])
what is the number of Rs between the mid R and the R we're moving? => (mid - i)

the majority of this answer is understanding THAT formula.
'''


def min_swaps_to_group_balls(s):
    idxs = []
    for i in range(len(s)):
        if s[i] == "R":
            idxs.append(i)
    mid = len(idxs)//2
    result = 0
    for i in range(len(idxs)):
        result += abs(idxs[i] - idxs[mid]) - abs(mid - i)
    return result

datas = [
    ("RWWWWR", 4),
    ("WRRWWR", 2),
    ("RWRWRWR", 4),
    ("WWW", 0),
    ("RRR", 0),
    ("WRWWRWRWWR", 6)
]

for data in datas:
    try:
        assert (min_swaps_to_group_balls(data[0]) == data[1])
        print(f"assertion passed at {data[0]} for {data[1]}")
    except AssertionError:
        print(f"assertion failed at {data[0]} for {data[1]}")