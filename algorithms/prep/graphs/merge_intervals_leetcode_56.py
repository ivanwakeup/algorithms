'''
THE OVERALL RUNTIME OF SOLVING MERGE INTERVALS THIS WAY IS QUADRATIC!
it takes 0(n^2) time in the worst case to build the graph, if all successive intervals in our double for
loop are overlapping.

lets build a graph of the intervals first.

if an interval overlaps with another, lets connect the intervals by an edge

example graph output:

{
"1:3": {[2,6]},
"2:6": {[1,3]},
"8:10": {},
"15:18": {}
}
can we build a graph of unsorted intervals in linear time?
no i dont think so, even if we used a set we'd have to check each interval
against each other it might overlap with

sort the intervals first and add each interval to graph
now mergable intervals appear near each other

curr = first interval
if curr can merge with high pointer, add edge to graph

we need to return all the components that are connected together. how can we get them?

do a dfs from each vertex, everything we can reach from that vertex is part of SCC? 
for an undirected graph this is true. for a directed, not necessarily.

proof:
true because no matter where i add a node to an undirected graph that is already a tree, we can reach it from any node we start at.
if we can't reach it from the existing tree, it must not be connected to anything and is not part of an SCC


procedure:
perform DFS from every vertex V in graph G
at start, at current vertex V to strongly output list
along the way, add each node we can reach to the same component
once we're done with this dfs tree, add CURR to result

repeat for each vertex V and return resulting list

this only takes linear time in the number of intervals we have, despite the double for loop
because if ALL intervals overlap from constructing the graph, we'll only have 1 list in the list of lists
eg:
[[1,3],[2,5],[4,4]]
'''


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

iv = [Interval(1, 3), Interval(2,6), Interval(8,10), Interval(15,18)]

class Solution(object):

    def merge(self, intervals):
        tups = self.ints_to_tup(intervals)
        g = self.build_graph(tups)
        strong = self.get_strong_components(g)
        ints = self.get_merged_intervals(strong)
        return self.list_to_ints(ints)

    def build_graph(self, intervals):
        list.sort(intervals, key=lambda x: x[0])
        graph = {}
        for interval in intervals:
            graph[interval] = set()

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[i][1] >= intervals[j][0]:
                    graph[intervals[i]].add(intervals[j])
                    graph[intervals[j]].add(intervals[i])

        return graph

    def get_strong_components(self, graph):
        visited = set()
        result = []

        def dfs(vertex, curr):
            visited.add(vertex)
            curr.append(vertex)
            for neigh in graph[vertex]:
                if neigh not in visited:
                    dfs(neigh, curr)

        for key in graph.keys():
            if key not in visited:
                curr = []
                dfs(key, curr)
                result.append(curr)
        return result

    def get_merged_intervals(self, strong_components):
        res = []
        for ls in strong_components:
            cur_min = float('inf')
            cur_max = float('-inf')
            for item in ls:
                cur_min = min(cur_min, item[0])
                cur_max = max(cur_max, item[1])
            res.append([cur_min, cur_max])
        return res

    def ints_to_tup(self, intervals):
        return [(item.start, item.end) for item in intervals]

    def list_to_ints(self, ls):
        return [Interval(tup[0], tup[1]) for tup in ls]


sol = Solution()
print(sol.merge(iv))