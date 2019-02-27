'''
<<<<<<< HEAD
given a DAG representing tasks, find how long it will take to run them all

some can run in parallel (given by the DAG), we basically need to find the longest path from vertex X to vertex Y (the end)

the longest cost path is effectively the same as the shortest cost path if we invert all of the costs
'''

class Vertex:

    def __init__(self, data):
        self.data = data
        self.distance = float('inf')
        self.parent = None
        self.start_time = None
        self.end_time = None

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


a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')
f = Vertex('F')
h = Vertex('H')


dag = {
    a: {(c, 1), (b, 2)},
    b: {(d, 6)},
    c: {(d, 5)},
    d: {(e, 8)},
    e: set(),
    f: {(e, 7)},
    h: {(f, 2)}
}

'''
1. does topological sorting work for directed graphs with cycles? NO, because we'd never finish the nodes that are in a cycle
'''
def get_topological_order(dag):
    time = {'val': 0}
    visited = set()

    def dfs(vertex):
        time['val'] += 1
        visited.add(vertex)
        vertex.start_time = time['val']
        for neigh in dag[vertex]:
            if neigh[0] not in visited:
                dfs(neigh[0])

        time['val']+=1
        vertex.end_time = time['val']

    for key in dag.keys():
        if key not in visited:
            dfs(key)

    result = []
    for key in dag.keys():
        result.append(key)

    return sorted(result, key=lambda x: x.end_time, reverse=True)


topo_order = get_topological_order(dag)


'''
if we process nodes in topological order, the first node we process will have NO incoming edges, so its dist is 0

'''
def shortest_path_in_dag(dag, nodes, target, negate=False):
    #we first need to calculate all the nodes which have no incoming edges, so we can init their
    #distance to zero
    for node in nodes:
        node.distance = 0
    for node in nodes:
        for edge in dag[node]:
            weight = edge[1]
            if negate:
                weight*=-1
            new_dist = (node.distance + weight)
            edge[0].distance = min(edge[0].distance, new_dist)

    return target.distance

print(shortest_path_in_dag(dag, topo_order, e, True))


