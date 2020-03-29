'''

intuitions:
this is a straightforward BFS, considering the directions we can move as "neighbors" of the current node.

one interesting finding with implementing this BFS was i noticed that you MUST mark a neighbor as visited
BEFORE you enqueue it. otherwise, you risk adding the same node to the queue twice--> consider the case
where the "left" and "right" neighbors of the current node are the SAME node!
'''
from typing import List
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [0 for _ in range(len(arr))]
        q = deque([start])
        visited[start] = 1
        while q:
            node_idx = q.popleft()
            if not arr[node_idx]:
                return True
            left, right = node_idx - arr[node_idx], node_idx + arr[node_idx]
            if left>=0 and not visited[left]:
                visited[left] = 1
                q.append(left)
            if right < len(arr) and not visited[right]:
                visited[right] = 1
                q.append(right)
        return False

sol = Solution()
print(
    sol.canReach([58,48,64,36,19,19,67,13,32,2,59,50,29,68,50,0,69,31,54,20,22,43,30,9,68,71,20,22,48,74,2,65,27,54,30,5,66,24,64,68,9,31,50,59,15,72,6,49,11,71,12,61,5,66,30,1,2,39,59,35,53,21,76,17,71,40,68,57,64,53,70,21,50,49,25,63,35],
                 46)
)