from collections.abc import Hashable

class Vertex:

    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent

    def __repr__(self):
        return self.val
    #
    # def __hash__(self):
    #     return hash(self.val)


a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')
f = Vertex('F')

graph = {
    a: {b},
    b: {d},
    c: {a, b},
    d: {},
    e: {f},
    f: {e, d}
}

'''
g' = g transpose
basically swap edges
0(V+E) time
'''
from collections import defaultdict
def get_transpose_graph(g):
    result = defaultdict(set)
    for key in g.keys():
        for val in g[key]:
            result[val].add(key)
    return result

# dd = get_transpose_graph(graph)
# print(dd)

def print_graph_dfs(g):
    visited = set()
    def dfs(g, start):
        print(start.val)
        for neigh in g[start]:
            if neigh not in visited:
                visited.add(neigh)
                dfs(g, neigh)
    for key in g.keys():
        if key not in visited:
            print(f"starting DFS for start node {key}")
            visited.add(key)
            dfs(g, key)


#print_graph_dfs(graph)


'''
kruskals algorithm effectively works as follows:

we use a union-find structure to make sure we don't include nodes that would form a CYCLE in the minimum spanning tree
    - if a new edge that we're considering adding is part of an existing set in union-find, we discard it
    
    
WHY DO WE DISCARD EDGES THAT FORM CYCLES?
because if the edge forms a cycle, we can already reach every node in the subset of nodes we're considering.

we process the nodes in sorted order by edge cost, this will lead us to the minimum spanning tree
    - this also ensures we don't pick higher cost edges that would create a cycle 
'''

class UnionFindVertex(Vertex):

    def __init__(self, val):
        super(UnionFindVertex, self).__init__(val)
        self.size = 1
        self.parent = None

a = UnionFindVertex('A')
b = UnionFindVertex('B')
c = UnionFindVertex('C')
d = UnionFindVertex('D')
e = UnionFindVertex('E')
f = UnionFindVertex('F')

elements = [a, b, c, d, e, f]

#e[0] = cost, e[1] = v1, e[2] = v2
edges = [
    [3, a, c],
    [4, d, b],
    [2, e, f],
    [5, a, b],
    [6, c, e],
    [4, f, d],
    [3, b, f]
]
'''
naive find, no path compression
'''
def find(vertex):
    prev = vertex
    res = vertex.parent
    while res:
        prev = res
        res = res.parent
    return prev


'''
if we update the parent pointers when we find a vertex
'''
def find_with_path_compression(vertex):
    prev = vertex
    while vertex.parent:
        prev = vertex
        vertex = vertex.parent
        if vertex.parent:
            prev.parent = vertex.parent
    return prev


def union(edge):
    v1 = find(edge[1])
    v2 = find(edge[2])
    if v1 == v2:
        return
    newsize = v1.size + v2.size
    if v1.size > v2.size:
        v2.parent = v1
    elif v2.size > v1.size:
        v1.parent = v2
    else:
        v2.parent = v1
    v1.size = newsize
    v2.size = newsize

def kruskal_spanning_tree(edge_list):
    list.sort(edge_list, key=lambda x: x[0])
    spanning_edges = []
    for e in edge_list:
        if not find(e[1]) == find(e[2]):
            union(e)
            spanning_edges.append(e)
    return spanning_edges

print(kruskal_spanning_tree(edges))
