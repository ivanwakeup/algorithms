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

'''

input = [
    ["R", "R", "D"],
    ["L", "L", "L"],
    ["U", "U", "R"]
]


from collections import defaultdict
def create_graph(matrix):
    g = defaultdict(set)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            key = f"{str(r)}:{str(c)}"
            neighs = get_neighbors(matrix, r, c)
            for neigh in neighs:
                if neigh[0] == matrix[r][c]:
                    g[key].add((0, neigh[1], neigh[2]))
                else:
                    g[key].add((1, neigh[1], neigh[2]))
    return g


def get_neighbors(matrix, r, c):
    neighs = set()
    for item in (("D", r+1, c), ("R", r, c+1), ("U", r-1, c), ("L", r, c-1)):
        if inbounds(item[1], item[2], matrix):
            neighs.add(item)
    return list(neighs)

def inbounds(r, c, matrix):
    return r>=0 and c >=0 and r < len(matrix) and c < len(matrix[0])


g = create_graph(input)

from collections import deque

def zero_one_bfs(graph, target):
    start = "0:0"
    q = deque()
    q.append((0,start))
    visited = {start}
    total = 0
    while q:
        cost, node = q.pop()
        if node == target:
            return total
        total+=cost
        for neigh in graph[node]:
            neigh_key = f"{neigh[1]}:{neigh[2]}"
            if neigh_key not in visited:
                if neigh[0] == 0:
                    q.append((0, neigh_key))
                else:
                    q.appendleft((1, neigh_key))
                visited.add(neigh_key)
    return total


print(zero_one_bfs(g, "2:2"))
