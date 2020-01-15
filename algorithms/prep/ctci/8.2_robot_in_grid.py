'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.

restate problem:
we have a robot at a starting position in a matrix, and we need to find him a path to the end

ideas:
we could use a DFS to find a path, just checking boundaries along the way (We keep track of the  current path with an arrays_and_strings)
DFS would check almost every cell in the worst case, r*c complexity

there might be multiple valid paths?

0 0 x 0
0 0 0 0
0 0 x 0

two paths in this example: one of length 5 and one of 7

alternatives:

instead, we could compute the path from the end matrix[-1][-1]

a path from matrix[-1][-1] must include a path from matrix[-2][-1] or matrix[-1][-2]....and so on


algorithm:
path(matrix, matrix[end][end]) = if exists path(matrix, matrix[end-1][end], cur_path) then cur_path + matrix[end][end]
or if exists path(matrix, r, c-1) then same

'''

matrix = [
    [0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0]
]

def find_path(matrix):

    def do_find(matrix, r, c, result, memo):

        if r < 0 or c < 0 or matrix[r][c] == 1:
            return False

        key = (r,c)
        if key in memo:
            print("found memo!")
            return False

        at_origin = (r == 0) and (c == 0)
        if at_origin or do_find(matrix, r-1, c, result, memo) or do_find(matrix, r, c-1, result, memo):
            result.append(key)
            print("find path! row {} and col {}".format(r,c))
            return True

        memo.add(key)
        return False

    result = []
    memo = set()
    do_find(matrix,  len(matrix)-1, len(matrix[0])-1, result, memo)
    return result

print(find_path(matrix))


'''
we've gone from a 2^(r+c) to an r*c solution, because with the memoization we only need to consider each path once
'''