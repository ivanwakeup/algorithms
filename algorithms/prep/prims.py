class GraphVertex:

    def __init__(self, data):
        self.data = data
        self.distance = float('inf')
        self.parent = None
        self.edges = []

    def __str__(self):
        return "Vertex {}".format(self.data)

    def __repr__(self):
        return self.data

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return ord(self.data)

    def __lt__(self, other):
        return ord(self.data) < ord(other.data)


# class UndirectedGraphEdge:
#
#     def __init__(self, v1, v2, cost=None):
#         self.v1 = v1
#         self.v2 = v2
#         self.cost = cost
#
#     def __str__(self):
#         return "Graph Edge between {} to {} with cost {}".format(self.v1, self.v2, self.cost)
#
#     def __eq__(self, other):
#         return other.v1.data == self.v1.data and other.v2.data == self.v2.data
#
#     def __hash__(self):
#         return ord(self.v1.data) + ord(self.v2.data)
#
#     def __repr__(self):
#         return self.v1.data + ":" + self.v2.data
#
#
# class Graph:
#     adj_matrix = [
#            # A  B  C  D  E  F  G
#             [0, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 1, 1],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 1, 0],
#             [0, 0, 0, 0, 0, 0, 1],
#             [0, 0, 1, 0, 0, 0, 1],
#             [0, 0, 0, 0, 1, 0, 0]
#         ]
#
#     def __init__(self):
#         self.verticies = set()
#         self.start = None
#
#     @staticmethod
#     def build_from_adj_matrix(matrix):
#         import random
#         result = Graph()
#         for row in range(len(matrix)):
#             char = chr(65 + row)
#             v1 = GraphVertex(char)
#             for col in range(len(matrix[0])):
#                 if matrix[row][col] == 1:
#                     v2 = GraphVertex(chr(65 + col))
#                     if v2 not in [edge[0] for edge in v1.edges]:
#                         v1.edges.append((v2, random.randint(1,12)))
#             if v1 not in result.verticies:
#                 result.verticies.add(v1)
#             if not result.start:
#                 result.start = v1
#         return result
#
# g = Graph.build_from_adj_matrix(Graph.adj_matrix)
# print(g.verticies)
# for vert in g.verticies:
#     print(vert, vert.edges)
#
#
# def prims(graph):
#     visited = set()
#     node = graph.start
#     import queue
#     pq = queue.PriorityQueue()
#     pq.put((0, node))
#     while not pq.empty():
#         prio, node = pq.get()
#         visited.add(node)
#         if node.parent:
#
#         for neigh, cost in node.edges:
#             if neigh not in visited:
#                 if cost < neigh.distance:
#                     neigh.distance = cost
#                 neigh.parent = node
#                 pq.put((cost, neigh))
#     return visited
#
# print(prims(g))

# class Prims:
#
#     def __init__(self):
#         self.adj_matrix = [
#             #A  B  C  D  E  F  G
#             [0, 1, 0, 0, 0, 0, 0],
#             [1, 0, 0, 1, 0, 1, 1],
#             [0, 0, 0, 0, 0, 1, 0],
#             [0, 1, 0, 0, 0, 1, 0],
#             [0, 0, 0, 0, 0, 0, 1],
#             [0, 1, 1, 1, 0, 0, 1],
#             [0, 1, 0, 0, 1, 1, 0]
#         ]
#         self.verticies = self.build_verticies_from_adj_matrix(self.adj_matrix)
#
#     def build_verticies_from_adj_matrix(self, matrix):
#         result = set()
#         for row in range(len(matrix)):
#             char = chr(65 + row)
#             vert = Vertex(char)
#             for col in range(len(matrix[0])):
#                 if matrix[row][col] == 1:
#                     vertex = Vertex(chr(65+col))
#                     vert.adj[vertex] = ()
#             result.add(vert)
#         return result
#
#     def get_MST(self):
#         visited = set()
#         result = {}
#         import queue
#         pq = queue.PriorityQueue()
#         pq.put(())
#         #how to represent min spanning tree?
#         start = self.verticies.pop()
#
#
# prim = Prims()


A = GraphVertex('A')
B = GraphVertex('B')
C = GraphVertex('C')
D = GraphVertex('D')
E = GraphVertex('E')
F = GraphVertex('F')
G = GraphVertex('G')

graph = {
    A: [(B, 1)],
    B: [(D, 4), (G, 3), (F, 10)],
    C: [],
    D: [(F, 7)],
    E: [],
    F: [(C, 4)],
    G: [(E, 4)]
}

def prims(graph, start):
    unvisited = set(graph.keys())
    mst_edges = set()
    import queue
    pq = queue.PriorityQueue()
    pq.put((0, start))
    while not pq.empty() and unvisited:
        cost, node = pq.get()
        unvisited.remove(node)
        if node.parent:
            mst_edges.add((node.parent, node, cost))
        for neigh, path_cost in graph[node]:
            if neigh.distance > path_cost:
                neigh.distance = path_cost
            neigh.parent = node
            pq.put((neigh.distance, neigh))
    return mst_edges

print(prims(graph, A))