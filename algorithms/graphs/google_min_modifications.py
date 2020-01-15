'''
Given a matrix of direction with L, R, U, D, at any point you can move to the direction which is written over the cell [i, j]. We have to tell minimum number of modifications to reach from [0, 0] to [N - 1, M - 1] .

Example :-
R R D
L L L
U U R
Answer is 1, we can modify cell [1, 2] from L To D.

PS: I was not able to solve it during the interview, but in the end of the interview I got a nice idea to solve the problem but interviewer was not interested in listening as time was up and I was not 100% sure about that so I did not insist but later I found that was the correct solution.
I want to see how other people solve this problem, I will reveal the answer later, with time complexity of O(N * M)


first, we need to create the graph!


what IS the thought process here?
first, it's recognizing that we can encode a move from one cell to another with a 0 or 1.
either we can make the move for free (corresponding to a 0 move) or we have to change the direction of our current cell
to make it! (corresponding to a 1)

obviously, we need the knowledge of a 0-1 BFS to solve it. why does a 0-1 bfs work?

because this algorithm works like djikstras algorithm in that:
1. the next item we pop is ALWAYS the shortest path TO THAT ITEM

'''

from collections import deque


class ShortestPathVertex:

    def __init__(self, r, c):
        self.key = f"{str(r)}:{str(c)}"
        self.min_cost = 0
        self.neighbors = set()

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return self.key


def create_graph(matrix):
    graph = {}
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            v = ShortestPathVertex(r, c)
            graph[v.key] = v
            neighs = get_neighbors(matrix, r, c)
            for neigh in neighs:
                nv = ShortestPathVertex(neigh[1], neigh[2])
                if neigh[0] == matrix[r][c]:
                    v.neighbors.add((0, nv))
                else:
                    v.neighbors.add((1, nv))
    return graph


def get_neighbors(matrix, r, c):

    def inbounds(r, c, matrix):
        return 0 <= r < len(matrix) and 0 <= c <= len(matrix[0])

    neighs = []
    for item in (("D", r+1, c), ("R", r, c+1), ("U", r-1, c), ("L", r, c-1)):
        if inbounds(item[1], item[2], matrix):
            neighs.append(item)
    return neighs


def zero_one_bfs(graph, start, target):
    q = deque()
    q.append((0,start))
    visited = {start}
    while q:
        cost, node = q.pop()
        if node.key == target:
            return node.min_cost
        for cost, neigh in graph[node.key].neighbors:
            neigh.min_cost = cost + node.min_cost
            if neigh.key not in visited:
                if cost == 0:
                    q.append((0, neigh))
                else:
                    q.appendleft((1, neigh))
                visited.add(neigh.key)
    return -1


input = [
    ["D", "U", "L"],
    ["D", "L", "L"],
    ["U", "U", "R"]
]
g = create_graph(input)

print(zero_one_bfs(g, g["0:0"], "2:2"))
