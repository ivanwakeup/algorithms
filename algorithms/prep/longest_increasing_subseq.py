'''
at each position i, if i+1 > i then LIS(arr, i) = 1 + LIS(arr[i+1:]) else just LIS(i+1)

LIS(arr) = l
'''

def lis(arr):
    memo = {}
    return do_lis_memoized(arr, -9999, 0, memo)


def do_lis_memoized(arr, prev, curpos, memo):

    #REMEMBER, THEY KEY YOU USE IN YOUR MEMO HAS TO "DISTINCTLY" represent subproblems. I was trying to use only str(curpos)
    #for the key here, but this produces the wrong answer because it will return a cached value regardless of
    #if you have updated "PREV" in the previous call
    key = str(prev) + ":" + str(curpos)
    if key in memo:
        #print("returning key!")
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


print(lis([10,9,2,5,3,7,101,18]))

'''
for each index i, calculating the longest possible subseq is:
DP[i] = max(DP[j]) for each 0<=j<i + 1)
result = max(DP[i] for all i)

how do subproblems solve the larger problem?
by storing DP[i], you're calculating the maximum possible LIS UP TO THAT POINT. so, to answer the original problem what you need to find is
maximum of each of those subproblems! this is because for any given arrays_and_strings, the maximum LIS may or may not include the ith value
'''
def bottom_up_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)
    result = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                # LIS is at least 2
                dp[i] = max(dp[i], dp[j] + 1)
                result = max(result, dp[i])

    return result


print(bottom_up_lis([10,9,2,5,3,7,101,18]))

