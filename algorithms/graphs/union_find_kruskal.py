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
