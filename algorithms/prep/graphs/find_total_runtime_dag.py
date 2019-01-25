'''
given a DAG representing tasks and their runtime,
find the length of time it would take to execute all of the tasks
'''

from algorithms.data_structures.vertex import Vertex

A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
D = Vertex("D")
E = Vertex("E")
F = Vertex("F")
G = Vertex("G")

#create a function to return a list of verticies with letters between A and Z and random costs between 1 and 10


'''
how do we build a random dag? create verticies with portion of the alphabet
assign random costs
add each vertex to a dictionary
how do we add edges such that we build a graph with no cycles? 
if we add an edge to some vertex J from some vertex I, we can't add the edge from J back to I

so, as we add edges in the dict, we also add the vertex of the edge we're starting from
to a CANT_ADD set in the key of the other vertex
'''
def build_pseudo_random_dag():
    from random import randint
    verticies = []
    for code in range(65, 76):
        vertex = Vertex(chr(code))
        vertex.cost = randint(1,10)
        verticies.append(vertex)
    graph = {}
    for vertex in verticies:
        #first is CANT_ADD set, second is edges
        graph[vertex] = ({vertex}, set())

    v_len = len(verticies) - 1
    for vertex in verticies:
        num_edges = randint(1,3)
        for i in range(num_edges):
            rand_idx = randint(0, v_len)
            neighbor = verticies[rand_idx]
            if neighbor not in graph[vertex][0]:
                graph[neighbor][0].add(vertex)
                graph[vertex][1].add(neighbor)


    for key in graph.keys():
        graph[key] = graph[key][1]

    return graph


graph = build_pseudo_random_dag()

print(graph)


