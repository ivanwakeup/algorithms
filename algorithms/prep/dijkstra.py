'''
will need graph with nodes and edges
edges are directed and have weights associated with them
how to represent graph?
use dict with Vertex objects
how is edge denoted?
    1. adjacency set of tuples with (edge, cost)
    2. Edge object with V1, V2, cost


questions to answer:
why doesn't dijkstras work on graphs with a cycle?
'''

class Vertex:

    def __init__(self, data):
        self.data = data
        self.distance = float('inf')

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


A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')

graph = {
    A: {(E, 1), (C, 9)},
    B: {(E, 3), (C, 10), (F, 45)},
    C: {(D,4)},
    D: {(A, 5)},
    E: {(B, 3), (D, 2)},
    F: set()
}

import queue

'''
return shortest cost path in GRAPH from NODE to TARGET

what does priority queue do here?
keeps the next node i want to visit at the top of the queue

pseudo:
start at source node
inspect neighbors, update their vertex.distance if its less than initial
add each neighbor to priority queue (the "priority" is the distance)
mark CURR node as visited
visited top neighbor from priority queue
if top neighbor is TARGET, stop....you've found the shortest cost path from source to target
'''
def dijkstra_cost_source_to_target_only(node, target, graph):
    q = queue.PriorityQueue()
    visited = set()
    node.distance = 0
    q.put((node.distance, node))
    while not q.empty():
        dist, curr = q.get()
        if curr == target:
            return dist
        for vertex, cost in graph[curr]:
            if cost + curr.distance < vertex.distance:
                vertex.distance = cost + curr.distance
            if vertex not in visited:
                q.put((vertex.distance, vertex))
        visited.add(curr)
    return float('inf')

def dijkstra_source_to_all_verticies(node, graph):
    q = queue.PriorityQueue()
    visited = set()
    node.distance = 0
    q.put((node.distance, node))
    while not q.empty():
        dist, curr = q.get()
        for vertex, cost in graph[curr]:
            if cost + curr.distance < vertex.distance:
                vertex.distance = cost + curr.distance
            if vertex not in visited:
                q.put((vertex.distance, vertex))
        visited.add(curr)
    for key in graph.keys():
        if key != node:
            print("Shortest Path from {} to {} costs {}".format(node.data, key.data, key.distance))


def a_star(node, target, graph):
    q = queue.PriorityQueue()
    visited = set()
    node.distance = 0
    q.put((node.distance, node))
    while not q.empty():
        dist, curr = q.get()
        for vertex, cost in graph[curr]:
            if cost + curr.distance < vertex.distance:
                vertex.distance = cost + curr.distance
            if vertex not in visited:
                q.put((vertex.distance, vertex))
        visited.add(curr)
    for key in graph.keys():
        if key != node:
            print("Shortest Path from {} to {} costs {}".format(node.data, key.data, key.distance))

#print(dijkstra_cost_source_to_target_only(A, C, graph))

#dijkstra_source_to_all_verticies(A, graph)


'''
questions:
1. why does dijkstras not work on graphs with negative edge weights?
2. 
'''
