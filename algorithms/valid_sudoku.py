class Solution:
    chked_cell = set()

    def isValidSudoku(self, board):

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    if not self.validate(board, r, c):
                        return False
        return True

    def validate(self, board, r, c):
        row_begin = (r // 3) * 3
        col_begin = (c // 3) * 3

        chk = board[r][c]
        for i in range(r + 1, len(board)):
            if board[i][c] == chk:
                return False

        for j in range(c + 1, len(board[0])):
            if board[r][j] == chk:
                return False

        if f"{row_begin}{col_begin}" not in self.chked_cell:
            seen = set()
            for row in range(row_begin, row_begin + 3):
                for col in range(col_begin, col_begin + 3):
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
            self.chked_cell.add(f"{row_begin}{col_begin}")
            print(f"checked {row_begin}{col_begin} ")

        return True

sol = Solution()
print(sol.isValidSudoku([[".",".",".",".","5",".",".","1","."],
                         [".","4",".","3",".",".",".",".","."],
                         [".",".",".",".",".","3",".",".","1"],
                         ["8",".",".",".",".",".",".","2","."],
                         [".",".","2",".","7",".",".",".","."],
                         [".","1","5",".",".",".",".",".","."],
                         [".",".",".",".",".","2",".",".","."],
                         [".","2",".","9",".",".",".",".","."],
                         [".",".","4",".",".",".",".",".","."]]))