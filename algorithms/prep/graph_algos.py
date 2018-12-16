class Vertex:

    def __init__(self, data):
        self.data = data
        self.distance = float('inf')
        self.parent = None
        self.begin = None
        self.end = None

    def __str__(self):
        return "Vertex {}".format(self.data)

    def __repr__(self):
        return self.data

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)

    def __lt__(self, other):
        return ord(self.data) < ord(other.data)

A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')
G = Vertex('G')

graph = {
    A: [(B, 1)],
    B: [(D, 4), (G, 3), (F, 10)],
    C: [],
    D: [(F, 7)],
    E: [],
    F: [(C, 4)],
    G: [(E, 4)]
}

def prims_algorithm_get_MST_edges(graph, start):
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

#print(prims_algorithm_get_MST_edges(graph, A))

'''
TOPOLOGICAL SORTING OF A DAG USING FINISHING TIMES METHOD
'''
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
    result = []
    visited = set()

    def dfs(vertex, result):
        visited.add(vertex.data)
        time['val'] += 1
        vertex.begin = time['val']
        for neighbor in dag[vertex]:
            if neighbor.data not in visited:
                dfs(neighbor, result)
        time['val'] += 1
        vertex.finish = time['val']
        print("vertex {} started at {} and ended at {}".format(vertex.data, vertex.begin, vertex.finish))
        result.append(vertex)

    for v in dag.keys():
        if v.data not in visited:
            dfs(v, result)

    return sorted([node.finish for node in result], reverse=True)

#print(find_topo_order(get_ready_dag))
'''
END TOPOLOGICAL SORTING
'''
from collections import defaultdict

def transpose_directed_graph(graph):
    graph_t = defaultdict(set)
    for key in graph.keys():
        for node in graph[key]:
            graph_t[node].add(key)
    return graph_t

#print(transpose_directed_graph(get_ready_dag))


def kahns_topo_sort(dag):

    def compute_indegrees_dag(dag):
        degrees = {}
        for key in dag.keys():
            if key not in degrees:
                degrees[key] = 0
            for node in dag[key]:
                if node in degrees:
                    degrees[node] += 1
                else:
                    degrees[node] = 1

        return degrees

    def kahns_topo(dag):
        items = compute_indegrees_dag(dag)
        #enqueue nodes with indegree 0
        q = [key for key in items.keys() if items[key] == 0]
        result = []
        while q:
            node = q.pop(0)
            result.append(node)
            for neighbor in dag[node]:
                items[neighbor] -= 1
                if items[neighbor] == 0:
                    q.append(neighbor)
        return result

    return kahns_topo(dag)


print(kahns_topo_sort(get_ready_dag))