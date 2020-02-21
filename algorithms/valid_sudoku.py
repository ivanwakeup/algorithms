class Solution:
    def isValidSudoku(self, board):
        chk = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if not self.col_valid(board, r, c) or not self.row_valid(board, r, c):
                    return False
                tr, tc = self.get_topleft(board, r, c)
                cell = "{}{}".format(tr, tc)
                if cell not in chk:
                    if not self.cell_valid(board, r, c):
                        return False
                    chk.add(cell)
        return True

    def col_valid(self, board, row, col):
        chk = board[row][col]
        if chk == ".":
            return True
        start = (row + 1) % len(board)
        while start != row:
            if board[start][col] == chk:
                return False
            start += 1
            start %= len(board)
        return True

    def row_valid(self, board, row, col):
        chk = board[row][col]
        if chk == ".":
            return True
        start = (col + 1) % len(board[0])
        while start != row:
            if board[row][start] == chk:
                return False
            start += 1
            start %= len(board[0])
        return True

    def cell_valid(self, board, row, col):
        row_begin, col_begin = self.get_topleft(board, row, col)

        seen = set()
        for r in range(row_begin, row_begin + 3):
            for c in range(col_begin, col_begin + 3):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        return True

    def get_topleft(self, board, r, c):
        return (r // 3) * 3, (c // 3) * 3
