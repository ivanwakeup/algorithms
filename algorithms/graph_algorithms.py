class Vertex:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return self.val

    def __hash__(self):
        return hash(self.val)


b = Vertex('B')
f = Vertex('F')
g = Vertex('G')
a = Vertex('A')
d = Vertex('D')
h = Vertex('H')
t = Vertex('T')

graph = {
    b: {f, g},
    f: {a},
    g: {a},
    a: {d, h},
    d: {},
    h: {t},
    t: {}
}

from collections import deque


def bfs(graph, start_node):
    queue = deque()
    queue.append(start_node)
    visited = {start_node}
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        for neigh in graph[node]:
            if neigh not in visited:
                queue.append(neigh)
                visited.add(neigh)
    print(result)


#bfs(graph, b)

'''
let's describe how UnionFind works again. we need to support a few operations:
find -> return WHICH set an edge(x, y) belongs to
union -> union two disjoint sets together

some additional heuristics:
path compression-> as we perform the find procedure, store the verticies we encounter along the way so
we can ultimately reset their parent pointers to the top of the tree, thus "flattening" the tree



'''


class UnionFindVertex(Vertex):
    
    def __init__(self, val):
        super(UnionFindVertex, self).__init__(val)
        self.parent = None
        self.rank = 0
        self.size = 1


a = UnionFindVertex('A')
b = UnionFindVertex('B')
c = UnionFindVertex('C')
d = UnionFindVertex('D')
e = UnionFindVertex('E')
f = UnionFindVertex('F')


def union(v1, v2):

    if v1.parent and v2.parent:
        v1.parent = v2 if v1.size < v2 else v2.parent = v1



