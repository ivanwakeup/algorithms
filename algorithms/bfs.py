graph = {'A': ['C', 'B'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


def bfs(graph, start):

    hit_order = []
    queue = [start]
    visited = [start]

    while queue:
        node = queue.pop(0)
        hit_order.append(node)

        neighbors = graph[node]
        for i in neighbors:
            if i not in visited:
                visited.append(i)
                queue.append(i)

    return hit_order


print(bfs(graph, 'A'))


class Solution:
    def longestPalindrome(self, s):
        longest = 0
        for i in range(len(s)):
            for j in range(1, len(s) + 1):
                if self.isPalindrome(s[i:j]):
                    longest = max(longest, j - i)
        return longest

    def isPalindrome(self, s):
        tmp = s[::-1]
        if tmp == s:
            return True
        return False
