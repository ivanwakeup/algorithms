def minPathSum(grid):
    return mps(grid, len(grid) - 1, len(grid[0]) - 1, {})

def mps(grid, i, j, memo):
    key = str(i) + ":" + str(j)
    if key in memo:
        return memo[key]
    if i < 0 or j < 0:
        return float('inf')
    if i == 0 and j == 0:
        return grid[i][j]

    result = grid[i][j] + min(mps(grid, i - 1, j, memo), mps(grid, i, j - 1, memo))
    memo[key] = result
    return result


'''
we can also do a bottom-up, and save the path.
of course, saving the path requires we use O(nm) space to do so,
because we have to traverse back up from the end position to find what our
min cost path was

we "find the path" by:
1. start at end
2. move to the (row, col) position with the best mps, and store that move
3. continue doing this until we're at 0, 0
'''

def bottom_up_with_path_mps(grid):
    if not grid:
        return float('inf')
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dp[0][0] = grid[0][0]
    for col in range(1,len(grid[0])):
        dp[0][col] = grid[0][col] + dp[0][col-1]
    for row in range(1, len(grid)):
        dp[row][0] = grid[row][0] + dp[row-1][0]

    for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
            dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]
    mps = dp[-1][-1]
    #now lets find the path
    path = []
    r, c = len(grid)-1, len(grid[0])-1
    while r >= 0 and c >= 0:
        path.insert(0, [r, c])
        if r <=0:
            c-=1
            continue
        if c <= 0:
            r-=1
            continue

        if dp[r-1][c] < dp[r][c-1]:
            r-=1
        else:
            c-=1

    return mps, path


print(bottom_up_with_path_mps([[1,2,3,1],[3,4,1,5],[7,6,2,1], [4,1,6,2]]))