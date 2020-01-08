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
#
# edges = [
#     (a, b),
#     (b, d),
#     (c, f),
#     (f, e),
#     (a, c),
#     (e, d)
# ]
edges = [
    (a, b),
    (d, c)
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

def union(edge):
    v1 = find(edge[0])
    v2 = find(edge[1])
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

for e in edges:
    if find(e[0]) != find(e[1]):
        union(e)

print(find(edges[0][1]))