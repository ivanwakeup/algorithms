
def maximalSquare( matrix):
    if not matrix:
        return 0

    max_square = 0
    rowL = len(matrix)
    colL = len(matrix[0])
    dp = [[0 for _ in range(colL)] for _ in range(rowL)]

    for i in range(colL):
        dp[0][i] = int(matrix[0][i])
        max_square = max(max_square, dp[0][i])

    for i in range(rowL):
        dp[i][0] = int(matrix[i][0])
        max_square = max(max_square, dp[i][0])

    for i in range(1, rowL):
        for j in range(1, colL):
            dp[i][j] = min(int(dp[i - 1][j]), int(dp[i][j - 1]), int(dp[i - 1][j - 1])) + int(
                matrix[i][j])
            max_square = max(max_square, dp[i][j])

    return max_square ** 2


data = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]

print(maximalSquare(data))