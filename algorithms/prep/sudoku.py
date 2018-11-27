board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]


def isValidSudoku(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '.':
                if not isValid(board[i][j], i, j, board):
                    return False
    return True


def isValid(num, row, col, board):
    cell_row = row // 3 * 3
    cell_col = col // 3 * 3
    for i in range(len(board)):
        if row == i:
            continue
        if board[i][col] == num:
            return False
    for j in range(len(board[0])):
        if col == j:
            continue
        if board[row][j] == num:
            return False
    for i in range(cell_row, cell_row + 3):
        for j in range(cell_col, cell_col + 3):
            if i == row and j == col:
                continue
            if board[i][j] == num:
                return False
    return True



data = [1]

def backtrack(arr, i, nums):
    if i == len(nums):
        return
    print(arr)
    for x in range(i, len(nums)):
        arr.append(nums[x])
        backtrack(arr, i+1, nums)

backtrack(data, 0, [1,2,3])

print(data)