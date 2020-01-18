'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].



INTUITIONS:
1. seems like a greedy problem because whatever characters have the HIGHEST counts we want to try using them up as much as possible first
so we can

plan:
add characters and their counts to max heap
pop a char, if its the same as the previous char:
    pop next char, if heap still exists
    return original char to heap
else:
    add char to result string
    reduce count
    add back to heap if still count

we know we've failed if we run out of heap items while our current char is the same as the previous

'''
import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        counts = Counter(S)
        heap = []
        for key in counts.keys():
            heapq.heappush(heap, [-counts[key], key])

        result = []
        while heap:
            item = heapq.heappop(heap)
            if result and item[1] == result[-1]:
                if not heap:
                    return ""
                nxt = heapq.heappop(heap)
                heapq.heappush(heap, item)
                item = nxt
            result.append(item[1])
            if item[0] < -1:
                heapq.heappush(heap, [item[0]+1, item[1]])

        return "".join(result)
