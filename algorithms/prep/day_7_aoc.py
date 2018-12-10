steps = '''
Step Q must be finished before step O can begin.
Step Z must be finished before step G can begin.
Step W must be finished before step V can begin.
Step C must be finished before step X can begin.
Step O must be finished before step E can begin.
Step K must be finished before step N can begin.
Step P must be finished before step I can begin.
Step X must be finished before step D can begin.
Step N must be finished before step E can begin.
Step F must be finished before step A can begin.
Step U must be finished before step Y can begin.
Step M must be finished before step H can begin.
Step J must be finished before step B can begin.
Step B must be finished before step E can begin.
Step S must be finished before step L can begin.
Step A must be finished before step L can begin.
Step E must be finished before step L can begin.
Step L must be finished before step G can begin.
Step D must be finished before step I can begin.
Step Y must be finished before step I can begin.
Step I must be finished before step G can begin.
Step G must be finished before step R can begin.
Step V must be finished before step T can begin.
Step R must be finished before step H can begin.
Step H must be finished before step T can begin.
Step S must be finished before step E can begin.
Step C must be finished before step E can begin.
Step P must be finished before step T can begin.
Step I must be finished before step H can begin.
Step O must be finished before step P can begin.
Step M must be finished before step L can begin.
Step S must be finished before step D can begin.
Step P must be finished before step D can begin.
Step P must be finished before step R can begin.
Step I must be finished before step R can begin.
Step Y must be finished before step G can begin.
Step Q must be finished before step L can begin.
Step N must be finished before step R can begin.
Step J must be finished before step E can begin.
Step N must be finished before step T can begin.
Step B must be finished before step V can begin.
Step Q must be finished before step B can begin.
Step J must be finished before step H can begin.
Step F must be finished before step B can begin.
Step W must be finished before step X can begin.
Step S must be finished before step T can begin.
Step J must be finished before step G can begin.
Step O must be finished before step R can begin.
Step K must be finished before step B can begin.
Step Z must be finished before step O can begin.
Step Q must be finished before step S can begin.
Step K must be finished before step V can begin.
Step B must be finished before step R can begin.
Step J must be finished before step T can begin.
Step E must be finished before step T can begin.
Step G must be finished before step V can begin.
Step D must be finished before step Y can begin.
Step M must be finished before step Y can begin.
Step F must be finished before step G can begin.
Step C must be finished before step P can begin.
Step V must be finished before step R can begin.
Step R must be finished before step T can begin.
Step J must be finished before step Y can begin.
Step U must be finished before step R can begin.
Step Z must be finished before step F can begin.
Step Q must be finished before step V can begin.
Step U must be finished before step M can begin.
Step J must be finished before step R can begin.
Step L must be finished before step V can begin.
Step W must be finished before step K can begin.
Step B must be finished before step Y can begin.
Step O must be finished before step N can begin.
Step D must be finished before step V can begin.
Step P must be finished before step B can begin.
Step U must be finished before step I can begin.
Step O must be finished before step T can begin.
Step S must be finished before step G can begin.
Step X must be finished before step A can begin.
Step U must be finished before step T can begin.
Step A must be finished before step I can begin.
Step B must be finished before step G can begin.
Step N must be finished before step Y can begin.
Step Z must be finished before step J can begin.
Step M must be finished before step D can begin.
Step U must be finished before step A can begin.
Step S must be finished before step R can begin.
Step Z must be finished before step A can begin.
Step Y must be finished before step R can begin.
Step E must be finished before step Y can begin.
Step N must be finished before step G can begin.
Step Z must be finished before step X can begin.
Step P must be finished before step X can begin.
Step Z must be finished before step T can begin.
Step Z must be finished before step P can begin.
Step V must be finished before step H can begin.
Step P must be finished before step L can begin.
Step L must be finished before step H can begin.
Step X must be finished before step V can begin.
Step W must be finished before step G can begin.
Step N must be finished before step D can begin.
Step Z must be finished before step U can begin.
'''

# steps =
# Step C must be finished before step F can begin.
# Step C must be finished before step A can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin.'''

class Graph:

    verticies = set()
    edges = set()

    def __str__(self):
        self.verticies = set()
        self.edges = set()

    def add_edge(self, edge_tuple):
        self.edges.add(edge_tuple)


class Vertex:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.begin = None
        self.end = None

    def __str__(self):
        return "Vertex {} with Parent {} and Child {}".format(self.data, self.parent, self.child)

    def __repr__(self):
        return self.data

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return ord(self.data)


def get_steps(step_str):
    step_sent = step_str.split("\n")
    res = []
    for sent in step_sent:
        tmp = [x for x in sent.split()]
        if tmp:

            res.append((tmp[1], tmp[-3]))
    return res

from collections import defaultdict
import queue


# def build_graph(edges):
#     g = defaultdict(list)
#     for edge in edges:
#         vertex = Vertex(edge[0])
#         v2 = Vertex(edge[1])
#         g[vertex].append(v2)
#     out = {}
#     for key in g.keys():
#         tmp = g[key]
#         l = sorted(tmp, key=lambda x:x.data)
#         out[key] = l
#
#     vertex = Vertex('E')
#     out[vertex] = []
#     return out

def build_graph(edges):
    g = {}
    for edge in edges:
        vertex = Vertex(edge[0])
        v2 = Vertex(edge[1])
        if vertex in g:
            g[vertex].add(v2)
        else:
            g[vertex] = {v2}
        if v2 not in g:
            g[v2] = set()
    return g


def topological_sort(dag):

    time = {'val': 0}

    def dfs(node):
        visited.add(node)
        time['val'] += 1
        node.begin = time['val']
        for neighbor in dag[node]:
            if neighbor not in visited:
                dfs(neighbor)
        time['val'] += 1
        node.end = time['val']

    visited = set()
    for key in dag.keys():
        if key not in visited:
            dfs(key)

    node_list = [key for key in visited]
    node_order = sorted(node_list, key=lambda x: x.end, reverse=True)
    return node_order


edge_set = get_steps(steps)
graph = build_graph(edge_set)
# order = topological_sort(graph)
# print(edge_set)
print(graph)
# print(order)
# print("".join([x.data for x in order]))


def kahns_topo(dag):
    result = []
    s = sorted(get_nodes_without_inc(dag), key=lambda x: x.data, reverse=True)
    print(s)
    while len(s) != 0:
        node = s.pop()
        result.append(node)
        for neighbor in get_neighbors(dag, node):
            dag[node].remove(neighbor)
            if neighbor in get_nodes_without_inc(dag):
                s.append(neighbor)
                s.sort(key=lambda x: x.data, reverse=True)
    return result

def get_neighbors(dag, node):
    return [x for x in dag[node]]

def get_nodes_without_inc(dag):
    result = []
    for key in dag.keys():
        contains = False
        for k2 in dag.keys():
            if key in dag[k2]:
                contains = True
                break
        if not contains:
            result.append(key)
    return result



result = kahns_topo(graph)

print("".join([x.data for x in result]))
