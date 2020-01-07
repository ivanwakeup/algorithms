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


bfs(graph, b)