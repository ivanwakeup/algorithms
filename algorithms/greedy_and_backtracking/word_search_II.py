'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


INTUITION:
this problem is mostly the same as word search. the addition of the trie structure helps us quickly find if one of the words
we're searching for exist. IF WE DIDN'T HAVE THE TRIE we'd need to:

pass the current suffixes of the words we're searching for at each level of the DFS
iterate through ALL the words to see if the current board[i][j] matches any of the first characters

for each match we


'''
class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        # make trie
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        self.res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board, i, j, trie, '')
        return list(self.res)

    def find(self, board, i, j, trie, pre):
        if '#' in trie:
            self.res.add(pre)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] != -1 and board[i][j] in trie:
            tmp = board[i][j]
            board[i][j] = -1
            self.find(board, i + 1, j, trie[tmp], pre + tmp)
            self.find(board, i, j + 1, trie[tmp], pre + tmp)
            self.find(board, i - 1, j, trie[tmp], pre + tmp)
            self.find(board, i, j - 1, trie[tmp], pre + tmp)
            board[i][j] = tmp
