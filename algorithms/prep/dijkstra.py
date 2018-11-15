class GraphNode:

    def __init__(self, key):
        self.key = key
        self.edges = set()

    def add_edge(self, edge):
        self.edges.add(edge)

    def add_node_edge(self, node, weight):
        edge = DirectedGraphEdge(self, node, weight)
        self.edges.add(edge)


class DirectedGraphEdge:

    def __init__(self, parent, child, weight):
        self.weight = weight
        self.parent = parent
        self.child = child

    def __lt__(self, other):
        return self.weight < other.weight


node1 = GraphNode('A')
node2 = GraphNode('B')
node3 = GraphNode('C')
node4 = GraphNode('D')
node5 = GraphNode('E')
node6 = GraphNode('F')
node7 = GraphNode('H')

node1.add_node_edge(node2, 5)
node1.add_node_edge(node3, 2)
node2.add_node_edge(node6, 3)
node3.add_node_edge(node5, 4)
node3.add_node_edge(node4, 2)
node4.add_node_edge(node5, 3)
node4.add_node_edge(node6, 4)
node5.add_node_edge(node7, 7)
node6.add_node_edge(node7, 6)

'''
use a priority queue which manages what nodes to visit based on their position in the queue. nodes with a lower edge cost
come first in the priority queue
termination: when target_node bubbles to the top of the priority queue

observations:
1. how to keep track of current cost of path?
2. 
'''
import heapq
def dijkstra_shortest_path(start_node, target_node):
    cost = float('inf')
    if not start_node or not target_node:
        return cost
    pq = [start_node.edges]
    heapq.heapify(pq)
    visited = {}
    while pq:
        edge = heapq.heappop(pq)
        edges = edge.child.edges
        local_cost = edge.weight
        #need to update the cost to
        visited[edge.child.key] = local_cost
        for edge in edges:
            if edge.child.key not in visited:
                heapq.heappush(pq, edge)




print(dijkstra_shortest_path(node1, node7))

