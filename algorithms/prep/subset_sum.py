data = [2,2,3,5]
target = 9


# def subset_sum_naive(arr, n, target):
#
#     if n == len(arr):
#         return target == 0
#
#     if target == 0:
#         return True
#
#     included = False
#     if target - arr[n] >= 0:
#         included = subset_sum_naive(arr, n+1, target-arr[n])
#     not_inc = subset_sum_naive(arr, n+1, target)
#     result = max(included, not_inc)
#     return result
#
#
# print(subset_sum_naive(data, 0, target))


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

#print(bottom_up_subset_sum(data, target))


def canPartition(nums):
    total = sum(nums)
    if not nums or total % 2:
        return False

    target = sum(nums) // 2
    dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]

    # can make a subset that sums to 0 from any number of elements
    for i in range(len(nums)):
        dp[i][0] = True

    for i in range(1, target + 1):
        dp[0][i] = True if nums[0] == i else False

    for row in range(1, len(nums)):
        for col in range(1, target + 1):
            if col - nums[row] >= 0:
                dp[row][col] = dp[row - 1][col - nums[row]]
            else:
                dp[row][col] = dp[row - 1][col]

            if col == target and dp[row][col]:
                return True

    return dp[-1][-1]


print(canPartition(data))


def canPartition_OPTIMIZED_LINEAR_SPACE(nums):
    total = sum(nums)
    if not nums or total % 2:
        return False

    target = sum(nums) // 2
    dp = [False] * (target + 1)
    dp[0] = True
    # can make a subset that sums to 0 from any number of elements

    for i in range(1, target + 1):
        dp[i] = True if nums[0] == i else False

    for row in range(1, len(nums)):
        cur = [True] + ([False] * (target + 1))
        for col in range(1, target + 1):
            if col - nums[row] >= 0:
                cur[col] = dp[col - nums[row]]
            else:
                cur[col] = dp[col]
            if col == target and cur[col]:
                return True
        dp = cur

    return dp[-1]