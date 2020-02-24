class Solution:
    def isValidSudoku(self, board):
        chk = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if not self.valid(board, r, c, "c") or not self.valid(board, r, c, "r"):
                    return False
                tr, tc = self.get_topleft(r, c)
                cell = "{}{}".format(tr, tc)
                if cell not in chk:
                    if not self.cell_valid(board, r, c):
                        return False
                    chk.add(cell)
        return True

    def valid(self, board, row, col, symbol):
        chk = board[row][col]
        if chk == ".":
            return True
        start = col+1 if symbol == "c" else row+1
        while start < 9:
            cmp = board[start][col] if symbol == "c" else board[row][start]
            if cmp == chk:
                return False
            start += 1
        return True

    def cell_valid(self, board, row, col):
        row_begin, col_begin = self.get_topleft(row, col)

        seen = set()
        for r in range(row_begin, row_begin + 3):
            for c in range(col_begin, col_begin + 3):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        return True

    def get_topleft(self, r, c):
        return (r // 3) * 3, (c // 3) * 3

sol = Solution()
sol.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])