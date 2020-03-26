'''
the answer is essentially the longest path on a BFS from a rotten node
to a non-rotten node

if a non-rotten node is unreachable (surrounded by blanks), then we return -1


'''

'''
travse graph to find nodes to enqueue
if any fresh node is found with no adajcent neighbors, return -1
if nothing queued, return -1

'''


class Solution:
    def orangesRotting(self, grid) -> int:
        result = 0
        q = []
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                neighs = self.get_neighs(grid, i, j)
                is_blank = all(grid[item[0]][item[1]] == 0 for item in neighs)
                if is_blank and grid[i][j] == 1:
                    return -1
                elif grid[i][j] == 2:
                    visited[i][j] = 1
                    q.append((i, j, 0))
        while q:
            i, j, level = q.pop(0)
            result = max(level, result)
            neighs = self.get_neighs(grid, i, j)
            for neigh in neighs:
                if not visited[neigh[0]][neigh[1]] and grid[neigh[0]][neigh[1]] == 1:
                    q.append((neigh[0], neigh[1], level + 1))
                    visited[neigh[0]][neigh[1]] = 1

        return result

    def get_neighs(self, grid, i, j):
        def inbounds(i, j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

        dirs = [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]
        return [x for x in dirs if inbounds(x[0], x[1])]


sol = Solution()
print(
    sol.orangesRotting([[1,2]])
)