from collections import defaultdict


class GraphNode:

    def __init__(self, val):
        self.value = val
        self.edges = set()
        self.ancestor = None

    def add_edge(self, graph_node):
        self.edges.add(graph_node)

    def __str__(self):
        return self.value


def buildAdj(pairs):
    hm = defaultdict(list)
    for pair in pairs:
        node = GraphNode(pair[0])
        neighbor = GraphNode(pair[1])
        hm[node] += [neighbor]
    return hm


# courses = [[1,0], [0,1], [1,2]]
#
# print(buildAdj(courses))

class Vertex:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.child = None
        #finishing time, useful for computing topological sort
        self.finish = None
        self.begin = None

    def __str__(self):
        return "Vertex {} with Parent {} and Child {}".format(self.data, self.parent, self.child)

    def __repr__(self):
        return self.data

# a = Vertex('A')
# b = Vertex('B')
# c = Vertex('C')
# d = Vertex('D')
# e = Vertex('E')
#
# dag1 = {
#      a : [(b, 1), (d, 3)],
#      d : [(d, 1)],
#      e : [(c, 3), (a, 5)],
#      b : [(a, 1)],
#      c : []
# }
#
# def find_all_cycles(graph):
#     #for all vertexes in the graph, run DFS while updating parents/childs. if you find child, you have cycle
#     cycles = set()
#     for node in graph.keys():
#         has_cycle(graph, node, [], [], cycles)
#     print(cycles)
#
# def has_cycle(graph, node, visited, rec, cycles):
#     visited.append(node.data)
#     rec.append(node.data)
#     for child, cost in graph[node]:
#         if child.data not in visited:
#             if has_cycle(graph, child, visited, rec, cycles):
#                 print("found cycle from {} to {}".format(node.data, child.data))
#                 cycles.add((node.data, child.data))
#                 return True
#         if child.data in rec:
#             cycles.add((node.data, child.data))
#             print("found cycle from {} to {}".format(node.data, child.data))
#             return True
#     rec.pop()
#     return False
#
# find_all_cycles(dag1)




underwear = Vertex('underwear')
pants = Vertex('pants')
belt = Vertex('belt')
shirt = Vertex('shirt')
tie = Vertex('tie')
jacket = Vertex('jacket')
socks = Vertex('socks')
shoes = Vertex('shoes')
watch = Vertex('watch')

get_ready_dag = {
    underwear: {pants, shoes},
    pants: {belt, shoes},
    belt: {jacket},
    shirt: {belt, tie, jacket},
    tie: {jacket},
    jacket: set(),
    socks: {shoes},
    shoes: set(),
    watch: set()
}

def find_topo_order(dag):
    #what order do i need to put things on to get ready?
    #perform dfs, keep track of finishing times
    time = {'val': 0}
    def dfs(vertex):
        visited.add(vertex.data)
        time['val'] += 1
        vertex.begin = time['val']
        for neighbor in dag[vertex]:
            if neighbor.data not in visited:
                dfs(neighbor)

        time['val'] += 1
        vertex.finish = time['val']
        print("vertex {} started at {} and ended at {}".format(vertex.data, vertex.begin, vertex.finish))
    visited = set()
    for v in dag.keys():
        if v.data not in visited:
            dfs(v)

# find_topo_order(get_ready_dag)
# result = sorted([item for item in get_ready_dag.keys()], key=lambda x: x.finish, reverse=True)
# for item in result:
#     print(item.data)


def get_strongly_components(dag):
    time = {'val': 0}

    def dfs(n_dag, vertex, visited):
        visited.add(vertex.data)
        time['val'] += 1
        vertex.begin = time['val']
        for neighbor in n_dag[vertex]:
            if neighbor.data not in visited:
                dfs(n_dag, neighbor, visited)
        time['val'] += 1
        vertex.finish = time['val']

    visited = set()
    for v in dag.keys():
        dfs(dag, v, visited)

    for v in dag.keys():
        print(v.data, v.begin, v.finish)

    dag_transpose = transpose(dag)
    sorted_keys = sorted([item for item in get_ready_dag.keys()], key=lambda x: x.finish, reverse=True)
    visited = set()

    print(dag)
    print(dag_transpose)
    for key in sorted_keys:
        dfs(dag_transpose, key, visited)


def transpose(dag):
    new_dag = {}
    for v in dag.keys():
        for adj in dag[v]:
            if adj in new_dag:
                new_dag[adj].add(v)
            else:
                new_dag[adj] = {v}
    for v in dag.keys():
        if v not in new_dag:
            new_dag[v] = set()

    return new_dag

# print(transpose(get_ready_dag))
# print(get_ready_dag)



def make_inf_adj(num_vertex):
    return [[float('inf') for _ in range(num_vertex+1)] for _ in range(num_vertex+1)]

graph = make_inf_adj(4)

#(from, to, weight)
edges = [(1, 3, -2), (2, 1, 4), (2, 3, 3), (3, 4, 2), (4, 2, -1)]


'''
why is this dynamic programming?

because this solution is based on the recurrence:

SP(i, j, k) = what is the shortest path from vertex i to vertex j that uses at most K other verticies as intermediary verticies?

its either a path that USES k verticies, in which case, you can define this path as:

SP(i, j, k) = SP(i, k, k-1) + SP(k, j, k-1)
in other words, if we're adding the kth vertex as an intermediary vertex, its the same as the SP(i, k) PLUS the SP(k, j)

OTHERWISE:

the SP just remains SP(i, j, k) = SP(i, j, k-1)

'''
def floyd_warshall(graph, edges):

    for f, t, w in edges:
        graph[f][t] = w

    #distance between a node and itself is 0
    for i in range(1, len(graph)):
        graph[i][i] = 0

    cardV = len(graph)

    for k in range(1, cardV):
        for i in range(1, cardV):
            for j in range(1, cardV):
                #if distance is greater, update it to the smaller value
                #you're checking if the that goes through the kth node is smaller than the smallest known distance from i to j
                #you'll never overwrite graph[i][i], because its already 0 cost for a node to itself
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    return graph


result = floyd_warshall(graph, edges)
for line in result:
    print(line)






