data = [3,34,4,12,5,2]
target = 9


def subset_sum_naive(arr, n, target):

    if n == len(arr):
        return target == 0

    if target == 0:
        return True

    included = False
    if target - arr[n] >= 0:
        included = subset_sum_naive(arr, n+1, target-arr[n])
    not_inc = subset_sum_naive(arr, n+1, target)
    result = max(included, not_inc)
    return result


print(subset_sum_naive(data, 0, target))


def bottom_up_subset_sum(arr, target):

    if not arr:
        return target == 0

    dp = [[False for _ in range(target+1)] for _ in range(len(arr)+1)]

    dp[0][0] = True

    for i in range(1, len(arr)+1):
        for j in range(1, target+1):
            if j - arr[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

print(bottom_up_subset_sum(data, target))