'''
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of
length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution.



Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
'''




'''
intuition:

the greedy way to do this is to start at any given person, and then continue iterating through the array to continue finding
people that match their group size, and add them until that group has been filled.


1. the question guarantees that a solution exists, which should help us realize that a greedy algorithm will lead us to 
a correct solution




'''
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        cnt = 0
        for i, ppl in enumerate(groupSizes):
            if cnt == len(groupSizes):
                return result
            if ppl < 0:
                continue

            result.append([])
            result[-1].append(i)
            groupSizes[i] = -1
            cnt += 1

            j = i + 1
            while j < len(groupSizes) and len(result[-1]) < ppl:
                if groupSizes[j] > 0 and groupSizes[j] == ppl:
                    result[-1].append(j)
                    cnt += 1
                    if cnt == len(groupSizes):
                        return result
                    groupSizes[j] = -1
                j += 1

        return result


'''
optimization:

we can just use a dictionary to store group size counts as the key

at each person, try and add them to dict[groupsize], once the group is full, just remove it
'''

'''
optimization:

use a defaultdict to store the ppl and groupcounts
as we iterate, we try to add person I to dict[groupSizes[i]], if its not full
if it becomes full, remove it from the dict and add it to the result


'''
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        result = []
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups[size])
                del groups[size]
        return result