'''
examples:

dynamic programming:
1. define problem recursively?
the max_sum array at position i = the max_arr either starts at i, or starts at some previous index and includes i, or terminates at i

if it terminates at i:
    dp[i] = max_so_far

if it includes i:
    dp[i] = dp[i-1] + nums[i]

if the max_subarray so far is negative, then we are basically just restarting the max_subarray (if what we have so far is negative, we CANT include anything up to this point, because its negative)

if its not negative, just include the current element

after updating dp[i] (dp[i] tells you what the max_subarray STARTING FROM THE FIRST NON-NEGATIVE position is), update the result = max(result, dp[i]), because dp[-1] wont always contain the max result (in the case where we already found a max subarray but had to reset the subarray at some dp[i])
'''


def maxSubArray(nums):
    if not nums:
        return 0
    dp = nums[0]
    result = dp
    for i in range(1, len(nums)):
        # update dp to be either the current element or append to the max_subarray so far if it isn't negative
        if dp < 0:
            dp = nums[i]
        else:
            dp = dp + nums[i]

        result = max(result, dp)
    return result


assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6



'''
this can also be solved non DP with the following observation:

any time we examine an element arr[i], we want to determine whether it is included or not:

the best we can do by including the i'th element is:
max(arr[i] + prev_with, arr[i])

and the best we can do by NOT including it is:
max(prev_with, prev_without)
'''

def maxSubArray_nonDP(nums):

    def mss(arr, i):
        if i == 0:
            return arr[i], arr[i]
        prev_with, prev_without = mss(arr, i - 1)

        return max(arr[i] + prev_with, arr[i]), max(prev_with, prev_without)

    if len(nums) == 1:
        return nums[0]
    return max(mss(nums, len(nums) - 1))


assert maxSubArray_nonDP([-2,1,-3,4,-1,2,1,-5,4]) == 6

