from collections import defaultdict

'''

'''
from collections import defaultdict

'''
we need to account for possible cycles in the graph as we relax edges

things to notice:
1. if no nodes have indegree 0 after building graph, we have a cycle
2. we can safely start traversing ANY nodes with indegree 0, as no cycle will be formed with those nodes
3. we have a cycle if we aren't able 
'''
from collections import deque

'''
we need to account for possible cycles in the graph as we relax edges

things to notice:
1. if no nodes have indegree 0 after building graph, we have a cycle
2. we can safely start traversing ANY nodes with indegree 0, as no cycle will be formed with those nodes
3. we have a cycle if we aren't able 
'''
from collections import deque
from typing import List

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         graph = self._build_graph(prerequisites, numCourses)
#         res = self._traverse(graph)
#         return res
#
#     def _build_graph(self, edges, courses):
#         g = {}
#         for i in range(courses):
#             if i not in g:
#                 g[i] = set()
#         for one, two in edges:
#             g[one].add(two)
#         return g
#
#     def _traverse(self, g):
#         result = []
#         q = deque()
#         for key in g.keys():
#             if len(g[key]) < 1:
#                 q.append(key)
#         while q:
#             node = q.popleft()
#             result.append(node)
#             if node in g:
#                 del g[node]
#             if not g:
#                 break
#             nxt = []
#             for key in g.keys():
#                 if node in g[key]:
#                     g[key].remove(node)
#                 if len(g[key]) == 0:
#                     nxt.append(key)
#             if not nxt:
#                 return []
#             for key in nxt:
#                 del g[key]
#             q.extend(nxt)
#         return result


'''
an optimized solution that uses linear space to keep track of indegree of each node.
in this way, we can easily just keep a count for a given node and how many edges it has coming into it
this is better than the above solution because we don't have to iterate over every key in the graph each
time we enter our while loop to see which nodes have indegree 0--we only need to iterate over the outgoing
edges from the current node we're considering.
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = self._build_graph(prerequisites, numCourses, indegree)
        res = self._traverse(graph, indegree)
        return res

    def _build_graph(self, edges, courses, indegree):
        g = {}
        for i in range(courses):
            if i not in g:
                g[i] = set()
        for one, two in edges:
            g[two].add(one)
            indegree[one] += 1
        return g

    def _traverse(self, g, indegree):
        result = []
        q = deque()
        visited = set()
        for idx in range(len(indegree)):
            if indegree[idx] == 0:
                q.append(idx)
                visited.add(idx)
        while q:
            node = q.popleft()
            result.append(node)
            for neighbor in g[node]:
                if neighbor in visited:
                    continue
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    visited.add(neighbor)

        return result if len(result) == len(indegree) else []



sol = Solution()
num = 3
data = []
print(
sol.findOrder(num, data)
)