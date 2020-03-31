'''
Given a string s consisting of n lowercase letters,
you have to delete the minimum number of characters from s so that every letter in s
appears a unique number of times.
We only care about the occurrences of letters that appear at least once in result.

Example 1:

Input: "eeeeffff"
Output: 1
Explanation:
We can delete one occurence of 'e' or one occurence of 'f'.
Then one letter will occur four times and the other three times.

examples:
"eeeefffff" => e appears 4 times and f appears 5 times, already uniq
"abcabc" => delete a once, and b twice
"aaabbbccc" => delete a twice, b once

"aabbcccddd" => [0,1,2,2]

"abbcccddd" => [0,1,1,2]


approach:
create a COUNTS array that stores the number of chars with a given count at count[i]
also create an array that stores the "available indexes" where a char at counts[i] could be placed.

while our counts[i]>1 and we have an available index to place the current char, our result+=i-avail_idxs[-1],
because this difference between the current index i and the first available index from the right represents
the number of occurences of char we'd have to delete to place the char in the counts[avail_idxs[-1]] position.

if we don't have any avail_idxs left, we must delete all occurences of the char being considered like:
result+=(counts[i]-1)*i


although we have a while loop to check avail_idxes, we'll never do more than 0(n) work because we only
have check the while condition at most N times--once we exhaust the available frequencies we stop needing
to loop
'''

from collections import Counter
def min_deletes_unique(s):
    c = Counter(s)
    counts = [0 for _ in range(len(s)+1)]
    max_cnt = 0
    for key in c.keys():
        counts[c[key]]+=1
        max_cnt = max(max_cnt, c[key])
    avail_idxs = []
    for i in range(max_cnt):
        if counts[i] == 0:
            avail_idxs.append(i)
    result = 0
    for i in range(1, max_cnt+1):
        while avail_idxs and counts[i]>1:
            counts[i]-=1
            result+=i-avail_idxs[-1]
            avail_idxs.pop()
        if counts[i]>1:
            result+=(counts[i]-1)*i

    return result


datas = [
    ("eeeeffff", 1),
    ("aabbcccddd", 4),
    ("zzzaabbcccddd", 7),
    ("aabbcccddd", 4),
    ("example", 4),
    ("llll", 0),
    ("aabbffddeaee", 6),
    ("abcdefhi", 7),
    ("", 0)
]

for data in datas:
    try:
        assert(min_deletes_unique(data[0]) == data[1])
        print(f"assertion succeeded for {data[0]} == {data[1]}")
    except AssertionError:
        print(f"assertion failed for {data[0]} == {data[1]}")


