'''
given a DAG, and a running time associated with each vertex
determine the minimum total runtime we can achieve by "executing" each task
assuming that non-dependent tasks can be parallelized
'''

class Vertex:
    def __init__(self, val, cost):
        self.val = val
        self.cost = cost
        self.indegree = 0

    def __repr__(self):
        return self.val

a = Vertex('A', 6)
b = Vertex('B', 4)
c = Vertex('C', 2)
d = Vertex('D', 2)
e = Vertex('E', 3)
f = Vertex('F', 7)
g = Vertex('G', 8)

graph = {
    a: {c, b},
    b: {c, d},
    c: {d},
    d: {},
    e: {c, f, d},
    f: {d},
    g: {e, f}
}

def calc_indegree(graph):
    for key in graph.keys():
        for v in graph[key]:
            v.indegree+=1

'''
this is a combination of kahn's algorithm for finding a topological ordering,
and just keeping track of the max runtime we encounter for each set of nodes
we're processing with indegree=0. if we just take the max of this subgroup of nodes
and add it to our total runtime, we end up with the minimum amount of time needed
to process the entire dag.

overall runtime should be theta(V+E), we need to consider each vertex and edge just once.
'''
def get_min_runtime(graph):
    queue = []
    for k in graph.keys():
        if k.indegree == 0:
            queue.append(k)
    nextq = []
    time = 0
    total = 0
    while queue:
        while queue:
            v = queue.pop(0)
            time = max(time, v.cost)
            for item in graph[v]:
                item.indegree-=1
                if item.indegree == 0:
                    nextq.append(item)
        total+=time
        if nextq:
            queue = nextq
            nextq = []
            time = 0
    return total

calc_indegree(graph)
print(get_min_runtime(graph))

