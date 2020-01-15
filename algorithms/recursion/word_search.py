def exist(board, word):
    if not word:
        return True
    if not board:
        return not word
    rowL = len(board)
    colL = len(board[0])


    for row in range(rowL):
        for col in range(colL):
            if board[row][col] == word[0]:
                visited = [[False for _ in range(colL)] for _ in range(rowL)]
                result = dfs(board, row, col, word, visited)
                if result:
                    return True
    return False


def dfs(board, r, c, word, visited):
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or visited[r][c]:
        return False
    if board[r][c] == word:
        return True
    elif board[r][c] != word[0]:
        return False
    visited[r][c] = True
    word = word[1:]
    return max(dfs(board, r + 1, c, word, visited), dfs(board, r - 1, c, word, visited), dfs(board, r, c + 1, word, visited), dfs(board, r, c - 1, word, visited))


board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]

word = "ABCESEFS"

print(exist(board, word))