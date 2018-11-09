'''
at each position i, if i+1 > i then LIS(arr, i) = 1 + LIS(arr[i+1:]) else just LIS(i+1)

LIS(arr) = l
'''

def lis(arr):
    memo = {}
    return do_lis_memoized(arr, -9999, 0, memo)


def do_lis_memoized(arr, prev, curpos, memo):
    key = str(prev) + ":" + str(curpos)
    if key in memo:
        return memo[key]

    if curpos == len(arr):
        return 0

    result_inc = 0
    if prev < arr[curpos]:
        result_inc = 1 + do_lis_memoized(arr, arr[curpos], curpos + 1, memo)
    result_not = do_lis_memoized(arr, prev, curpos + 1, memo)

    result = max(result_inc, result_not)
    memo[key] = result
    return result


print(lis([1,2,3,4,5,6]))

'''
for each index i, calculating the longest possible subseq is:
DP[i] = max(DP[j]) for each 0<=j<i + 1)
result = max(DP[i] for all i)

how do subproblems solve the larger problem?
by storing DP[i], you're calculating the maximum possible LIS UP TO THAT POINT. so, to answer the original problem what you need to find is
maximum of each of those subproblems! this is because for any given array, the maximum LIS may or may not include the ith value
'''
def bottom_up_lis(arr):
    if not arr:
        return 0

    dp = [0 for _ in range(len(arr)+1)]
    dp[0] = 1

    result = 1
    for i in range(1, len(arr)):
        local = 0
        for j in range(0, i):
            if arr[j] < arr[i]:
                local = max(local, dp[j])
            dp[i] = local + 1
            result = max(result, dp[i])
    return result


print(bottom_up_lis([10,9,12,1,6,5,3,8,9]))

