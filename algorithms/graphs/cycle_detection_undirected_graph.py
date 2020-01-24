'''

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.



INTUITION:
this is a straightforward cycle detection problem, which can be implemented with union find.
'''
class Solution:
    def findRedundantConnection(self, edges):
        def union(v1, v2):
            p1 = find(v1)
            p2 = find(v2)
            if p1 != p2:
                sets[p2] = p1
                return False
            return True

        def find(v):
            start = v
            while start != sets[start]:
                start = sets[start]
            return start

        sets = [0] + [ii + 1 for ii in range(len(edges))]
        for edge in edges:
            if union(edge[0], edge[1]):
                return edge





'''
alternative solution with recursive find routine. submitted by a leetcode user for problem redundant-connection leetcode 684
'''
# class Solution:
#     def findRedundantConnection(self, edges):
#         parent = [ii + 1 for ii in range(len(edges))]
#
#         def find(x):
#             if parent[x - 1] != x:
#                 parent[x - 1] = find(parent[x - 1])
#             return parent[x - 1]
#
#         def union(x, y):
#             rootx, rooty = find(x), find(y)
#             if rootx == rooty:
#                 return False
#             else:
#                 parent[rooty - 1] = rootx
#                 return True
#
#         for edge in edges:
#             x, y = edge
#             if not union(x, y):
#                 ans = edge
#         return ans


sol = Solution()

edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]

print(sol.findRedundantConnection(edges))



