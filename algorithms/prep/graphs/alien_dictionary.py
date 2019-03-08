'''

given an input dict of words, let's find the order of the language.


a few assumptions:

we are GUARANTEED to be able to determine the order of every letter based on the input. EG:
{"baa", "abcd", "abca", "cab", "cad"} = BDAC
{"baa", "abcd", "abca", "cab", "cad", "ef", "gt"} => can't determine the relative order of F and T, because each appear only once and both aren't the first letter of a word

so let's assume we won't have inputs that we can't determine total order

INPUT IS ALSO SORTED! this is crucial, because it means so long as we compare adjacent pairs (and assuming we're given at least enough info to determine relative order as highlighted
above), we can build a graph that shows which letter comes before the next by comparing pairs until we find a mismatch, adding an edge, then moving on to the next pair


to build this intuition of why comparing pairs works, here's some examples:
{"a", "e"} => comparing this pair yields A comes before E
{"ae", "ef"} => a still comes before e, but we can't know where f goes (doesn't appear in another pair or at the start of a word)
{"ae", "ef", "fa"} => AEF, pretty simple, just the comparision of w1 to w2 and w2 to w3 yields the graph with appropriate DIRECTED EDGES
{"ae", "ef", "faj"} => can't know j order
{"ae", "ef", "faj", "fje"} => now by comparing "faj" and "fje" we find a mismatch at char 2, and find a must come before j



assumptions:
1. if a is a prefix to b, a will appear before b in the dictionary
2. there may be multiple valid orderings, return any!

so basically, any valid topological order will work. if input is invalid, return empty string!


approach:
1. build graph with no edges from each letter by iterating over input
2. compare pairs Wsubi and Wsubi+1......Wsubn-1 and Wsubn until we find mismatching char
3. once find mismatch, and edge from w1 to w2 char in graph (if graph contains a back edge or cycle, input is invalid!)
4. once graph is built,
'''

#data = ["baa", "abcd", "abca", "cab", "cad"]
#data = ["baa", "abcd", "abca", "fad", "fda", "cab", "cad"]
data = ["fe", "fe", "ef", "gef", "agf" ]

'''
init VISITED, RESULT
calculate nodes with indegree 0, enqueue those
pop off queue, add to visited and result
inspect neighbor nodes, if indegree = 0, enqueue, else continue on

repeat until all nodes visited
if encounter a node in VISITED, there is a cycle so return ERROR


'''

class Vertex:

    def __init__(self, data):
        self.data = data
        self.distance = float('inf')
        self.indegree = 0
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


def kahns_topological_sort(graph):
    visited = set()
    result = []
    inverted = invert_adj_list_edges(graph)
    #build indegree from inverted graph
    for key in graph.keys():
        indeg = len(inverted[key])
        key.indegree = indeg

    queue = []
    for key in graph.keys():
        if key.indegree == 0:
            queue.append(key)
    while queue:
        node = queue.pop(0)
        result.append(node.data)
        visited.add(node)
        for neigh in graph[node]:
            if neigh in visited:
                raise ValueError("graph contains a cycle, no valid topological order possible")
            neigh.indegree -= 1
            if neigh.indegree == 0:
                queue.append(neigh)

    if len(result) != len(graph.keys()):
        raise ValueError("graph contains a cycle, no valid topological order possible")
    return result


def alien_dictionary(word_list):
    #now we have graph, so compare adjacent
    graph = {}
    for item in word_list:
        for char in item:
            if char not in graph:
                v = Vertex(char)
                graph[char] = v
    result = {}
    for i in range(len(word_list)-1):
        for j in range(len(word_list[i])):
            if j >= len(word_list[i+1]):
                continue
            if word_list[i][j] != word_list[i+1][j]:
                v1 = graph[word_list[i][j]]
                v2 = graph[word_list[i + 1][j]]
                if v1 in result:
                    result[v1].add(v2)
                else:
                    result[v1] = {v2}
                if v2 not in result:
                    result[v2] = set()
                break
    ordering = kahns_topological_sort(result)
    return ordering



'''
ex:
{ a: [b, c], b: [], c: [] } => { a: [], b: [a], c: [a] }

time complexity is really O(V + E), we have to traverse each adj list to build the new graph
but the outer for loop represents each V and inner for loop represents each E, for a total of E + V time
'''
def invert_adj_list_edges(graph):
    result = {}
    for key in graph.keys():
        if key not in result:
            result[key] = []
        for edge in graph[key]:
            if edge not in result:
                result[edge] = []
            result[edge].append(key)
    return result


out = alien_dictionary(data)
print(out)