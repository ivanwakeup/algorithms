'''
https://leetcode.com/problems/knight-probability-in-chessboard/
'''

'''
dp[i][j] answers what is the probability that the knight remains on the board if he moves from board[i][j]


'''


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1

        def is_inbounds(i, j):
            return i >= 0 and j >= 0 and i < N and j < N

        def inbounds(i, j):
            result = []
            directions = [(-2, 1), (-2, -1), (-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2)]
            for direc in directions:
                moved = (i + direc[0], j + direc[1])
                if is_inbounds(*moved):
                    result.append(moved)
            return result

        memo = {}

        def prob(K, i, j):
            key = str(K) + ":" + str(i) + ":" + str(j)
            if key in memo:
                return memo[key]
            if K == 1:
                ib = inbounds(i, j)
                return float(len(ib) / 8)

            result = float(len(inbounds(i, j)) / 8)
            probabilities = []
            for neigh in inbounds(i, j):
                probabilities.append(prob(K - 1, neigh[0], neigh[1]))

            res = result * (sum(probabilities) / len(probabilities)) if probabilities else result
            memo[key] = res
            return res

        return prob(K, r, c)


sol = Solution()
print(
    sol.knightProbability(3, 2, 0, 0)
)