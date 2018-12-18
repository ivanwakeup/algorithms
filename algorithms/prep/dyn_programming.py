def maximalSquare(matrix):
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        dp[i][0] = 1

    for j in range(len(matrix[0])):
        dp[0][j] = 1

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][col] == str(1) and matrix[row-1][col] == str(1) and matrix[row-1][col-1] == str(1) and matrix[row][col-1] == str(1):
                dp[row][col] = 1 + dp[row - 1][col - 1]
            else:
                dp[row][col] = dp[row - 1][col - 1]

    return dp[-1][-1] ** 2

data = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(data))