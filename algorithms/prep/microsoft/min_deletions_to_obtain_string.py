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


WE CAN SOLVE IT WITH A STACK!
approach:
any time we encounter a "BA" (B is at the top of the stack and A is our next character)
we definitely require 1 deletion.

you can kind of imagine "deleting" the "BA" from the string and concatenating the rest of the
string back together, and making sure it remains ordered.

so if our stack retains the property that it ONLY ever keeps characters that are already in the correct
order, we can just look at the next char in the string and see if it obeys that order by comparing it
to the last character we saw!

'''

from algorithms.utils import assert_test_cases

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


'''
we can actually ALSO solve this with by:
1. checking every possible partitioning of the array (of which there are n+1), and seeing how many chars
we would need to delete from either side
2. if we use a counter of chars, we can answer how many chars of B are present in the arr[:i], and how
many As are present in the arr[i+1:]? 
3. then we just keep track of the minimum of the result from #2 and that is our answer.
'''

from collections import Counter
def min_deletions_partitioning_approach(s):
    counts_right = Counter(s)
    counts_left = Counter()
    result = float('inf')
    for i in range(len(s)):
        result = min(result, (counts_left["B"] + counts_right["A"]))
        counts_right[s[i]]-=1
        counts_left[s[i]]+=1
    result = min(result, (counts_left["B"] + counts_right["A"]))
    return result


'''
we CAN also solve this with dynamic programming.

BA => 1
BBA => 2
ABAB => 1

ABA = 1
BBA = 1
BABA => 2


we have 3 main cases to handle:
1. current char is A and there are Bs before it, we could delete the current A and continue on OR delete all the Bs
2. current char is B, string is ok but keep track of the Bs we've seen in case we encounter an A
3. current char is an A and no Bs before, string is ok so continue on
'''


def min_deletions_dp(s):

    def find_min(s, i, b_count, memo):
        if i >= len(s):
            return 0

        key = str(i) + ":" + str(b_count)
        if key in memo:
            return memo[key]

        if s[i] == "A" and b_count:
            res = min(
                    (1 + find_min(s, i+1, b_count, memo)),
                    b_count + find_min(s, i+1, 0, memo)
                )
        elif s[i] == "B":
            res = find_min(s, i+1, b_count+1, memo)
        else:
            res = find_min(s, i + 1, b_count, memo)

        memo[key] = res
        return res

    result = find_min(s, 0, 0, {})
    return result



datas = [
    ("BBAAABA", 3),
    ("BBAA", 2),
    ("BAAABAB", 2),
    ("BBBAAA", 3),
    ("ABBBBBA", 1),
    ("AAAA", 0),
    ("BBBBB", 0),
    ("ABABAB", 2),
    ("BBBAAABAB", 4),
    ("BBBAAABBB", 3),
    ("B", 0),
    ("ABABABBBBBA", 3),
    ("ABBBAAABB", 3)
]

assert_test_cases(datas, min_deletions_dp)
assert_test_cases(datas, min_deletions_partitioning_approach)
assert_test_cases(datas, min_deletions)



