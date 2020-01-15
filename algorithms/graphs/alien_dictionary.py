'''
given a sorted dictionary of an alien language, find the order that each letter appears in the dictionary.


Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa"
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'




thoughts:

think about how a dictionary works
if we compare pairs of words starting from the beginning, the first mismatch tells us what character comes before another

can we learn of OTHER orderings by comparing additional letters in the word? NO, because:
1. the first mismatch letter determines the precendence for where the word appears in the dictionary. additional mismatches tell us nothing.
so in the first example:
b -> a
d-> a
a -> c
b -> d


approach:
traverse input list to create adj list of nodes

traverse again, compare pairs of words and characters. 0(n*k) runtime! n is length of input list and k is sum of length of all words

once adj list is built, just find a topological ordering of the input and that IS our order!
'''


def alien_dictionary(arr):
    if not arr:
        return []

    graph = {}
    for item in arr:
        for char in item:
            if char not in graph:
                graph[char] = set()

    for i in range(len(arr)-1):
        k = 0
        while (k < len(arr[i]) and k < len(arr[i+1])) and arr[i][k] == arr[i+1][k]:
            k+=1
        graph[arr[i][k]].add(arr[i+1][k])

    return topo_sort(graph)


'''
kahn's algorithm to relax edges:
0(V+E) time, there are only N edges in the graph where N is the number of pairs in the input

procedure:
start with vertex with no incoming edges, add to queue
inspect neighbors, relax those edges. if edge_count == 0, add to queue
after visiting neighbors, add vertex to result
'''
from collections import deque

def topo_sort(adj_list):
    visited = set()
    q = deque()
    result=[]
    flipped = flip_edges(adj_list)
    for key in flipped:
        if len(flipped[key]) == 0:
            visited.add(key)
            q.append(key)

    while q:
        node = q.popleft()
        for neighbor in adj_list[node]:
            flipped[neighbor].remove(node)
            if len(flipped[neighbor]) == 0:
                q.append(neighbor)
        result.append(node)

    if len(result) != len(adj_list):
        raise ValueError("no topo ordering possible!!")

    return result

'''
how to do this?

'''
from collections import defaultdict
def flip_edges(adj_list):
    result = defaultdict(set)
    for key in adj_list.keys():
        if key not in result:
            result[key] = set()
        for adj in adj_list[key]:
            result[adj].add(key)
    return dict(result)

adj_list = {
    "B": {"D", "A"},
    "D": {"A"},
    "A": {"C"},
    "C": set()
}


print(alien_dictionary(["baa", "abcd", "abca", "cab", "cad"]))