maze = [
    [1,1,1,1,0,1],
    [1,1,0,0,0,1],
    [0,0,0,1,0,1],
    [1,1,0,1,0,1],
    [1,0,0,1,0,1],
    [1,0,1,1,1,1],
    [1,0,0,0,1,1],
    [1,1,1,0,1,1]
]

def print_maze(maze):
    for item in maze:
        print(item)

class TwoDMazeSolver:

    def __init__(self, maze):
        self.maze = maze

    def solve(self):
        pass

    @staticmethod
    def find_start(maze):
        for i in range(len(maze[0])):
            if maze[0][i] == 0:
                return 0, i
        return -1,-1

    @staticmethod
    def check_bounds(row, col):
        if row < 0 or col < 0 or row >= len(maze) or col >= len(maze):
            return False
        if maze[row][col] == 1 or maze[row][col]==2:
            return False
        return True

    @staticmethod
    def get_surrounding(row, col):
        res = []
        for x, y in ((0,1), (1,0), (-1, 0), (0,-1)):
            res.append((row+x, col+y))
        return res

    @staticmethod
    def get_valid_moves(row, col, maze):
        if maze[row][col] == 1:
            return []
        surr = TwoDMazeSolver.get_surrounding(row,col)
        valid = [(x, y) for x,y in surr if TwoDMazeSolver.check_bounds(x, y)]
        return valid

import queue

def bfs_solve(maze):

    row, col = TwoDMazeSolver.find_start(maze)
    #maze is solved when you hit last row?
    q = queue.Queue()
    q.put((row, col))
    while q:
        r, c = q.get()
        maze[r][c] = 2
        if r == len(maze) -1:
            return
        surr = TwoDMazeSolver.get_surrounding(r, c)
        for nr, nc in surr:
            if TwoDMazeSolver.check_bounds(nr, nc):
                q.put((nr, nc))
    return


def dfs_backtrack(maze):

    def dfs(row, col, maze):
        if row == len(maze) - 1:
            maze[row][col] = 2
            return True
        maze[row][col] = 2
        surr = TwoDMazeSolver.get_surrounding(row, col)
        for nr, nc in surr:
            if TwoDMazeSolver.check_bounds(nr, nc):
                if dfs(nr, nc, maze):
                    return True
        maze[row][col] = 0
        return False

    # def dfs_iter(row, col, maze):
    #     stack = [(row, col)]
    #     cur_path = []
    #     while stack:
    #         r, c = stack.pop()
    #         cur_path.append((r,c, maze[r][c]))
    #         if r == len(maze) - 1:
    #             maze[r][c] = 2
    #             return
    #         maze[r][c] = 2
    #         surr = TwoDMazeSolver.get_valid_moves(r, c)
    #         if not surr:
    #             while cur_path:
    #                 nc, nr, val = cur_path.pop()
    #                 maze[nc][nr] = val
    #         else:
    #             for nr, nc in surr:
    #                 stack.append((nr,nc))
    #     return


    row, col = TwoDMazeSolver.find_start(maze)
    dfs(row,col,maze)


class Node:

    def __init__(self, row, col):
        self.r = row
        self.c = col
        self.parent = None

    def __repr__(self):
        return str(self.r) + ":" + str(self.c)

    def __eq__(self, other):
        return self.r == other.r and self.c == other.c

    def __hash__(self):
        return self.r*self.c

def is_junction(r, c):
    moves = set(TwoDMazeSolver.get_valid_moves(r, c, maze))
    if (r+1, c) in moves and (r, c+1) in moves:
        return True
    if (r-1, c) in moves and (r, c+1) in moves:
        return True
    if (r-1, c) in moves and (r, c-1) in moves:
        return True
    if (r+1, c) in moves and (r, c-1) in moves:
        return True
    if len(moves) == 1:
        if (r+1, c) not in moves:
            return True
    return False

def build_nodes(maze):
    # can you change row AND column? then yes, is junction
    #build the nodes from the input matrix
    r, c = TwoDMazeSolver.find_start(maze)
    start = Node(r, c)
    result = {start}
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if is_junction(row, col):
                result.add(Node(row, col))
    return result

def a_star_solve(nodes, maze):
    r, c = TwoDMazeSolver.find_start(maze)
    start = Node(r, c)
    visited = set()
    #how to build adj list?


print(build_nodes(maze))

#print(is_junction(4, 4))

#bfs_solve(maze)
#dfs_backtrack(maze)

print_maze(maze)

