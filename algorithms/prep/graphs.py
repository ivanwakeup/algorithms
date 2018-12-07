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
    underwear: [pants, shoes],
    pants: [belt, shoes],
    belt: [jacket],
    shirt: [belt, tie, jacket],
    tie: [jacket],
    jacket: [],
    socks: [shoes],
    shoes: [],
    watch: []
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

find_topo_order(get_ready_dag)
result = sorted([item for item in get_ready_dag.keys()], key=lambda x: x.finish, reverse=True)
for item in result:
    print(item.data)




