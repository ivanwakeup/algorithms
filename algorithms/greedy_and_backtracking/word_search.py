'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.



INTUITIONS:

the backtracking part comes from the fact that if we find board[i][j] != s[k], we don't need to perform any more
searches from that point of the search tree


'''


class Solution:
    def exist(self, board, word):

        def dfs(board, i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if board[i][j] != word[k]:
                return False

            if k >= len(word) - 1:
                return True

            # instead of creating a visited array, we just mark the current cell
            # as visited because we know nothing else further down the search tree
            # can use this node to form a valid word.
            board[i][j] = -1

            # big optimization by chaining the ORs. might substantially reduce the amount of DFSs
            # vs always performing all dfs's, if we find a true result early
            res = dfs(board, i, j - 1, k + 1) \
                  or dfs(board, i, j + 1, k + 1) \
                  or dfs(board, i + 1, j, k + 1) \
                  or dfs(board, i - 1, j, k + 1)

            # unmark it once we've completed the search tree, so future searches can search here again
            board[i][j] = word[k]

            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(board, row, col, 0):
                        return True

        return False


