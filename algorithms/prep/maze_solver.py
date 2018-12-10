maze = [
    [1,1,1,1,0,1],
    [1,1,0,0,0,1],
    [0,0,0,1,0,1],
    [1,1,0,1,0,1],
    [1,0,0,1,0,1],
    [1,0,1,1,1,1]
]

class TwoDMazeSolver:

    def __init__(self, maze):
        self.maze = maze

    def solve(self):
        pass

import queue

def bfs_solve(maze):

    def find_start(maze):
        for i in range(len(maze[0])):
            if maze[0][i] == 0:
                return 0, i
        return -1,-1

    def check_bounds(row, col):
        if row < 0 or col < 0 or row >= len(maze) or col >= len(maze):
            return False
        if maze[row][col] == 1:
            return False
        return True

    def get_surrounding(row, col):
        res = []
        for x, y in ((0,1), (1,0), (-1, 0), (0,-1)):
            res.append((row+x, col+y))
        return res

    row, col = find_start(maze)
    #maze is solved when you hit last row?
    q = queue.Queue()
    q.put((row, col))
    while q:
        r, c = q.get()
        maze[r][c] = 2
        if r == len(maze) -1:
            return
        surr = get_surrounding(r, c)
        for nr, nc in surr:
            if check_bounds(nr, nc):
                q.put((nr, nc))
    return


bfs_solve(maze)

print(maze)

