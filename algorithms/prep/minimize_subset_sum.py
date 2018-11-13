data = [1,6,11,5]
#min subsets are [1,6,5] and [11], absolute difference is abs(12 - 11) = 1

'''
observations:
could try every possible subset and see what the difference between their sums is!

'''

def all_subset_partitions(arr):

    if not arr:
        return []

    result = []
    for i in range(1,len(arr)-1):
        for j in range(i, len(arr)):
            left = data[:i] + [data[j]]
            right = data[i:j] + data[j+1:]
            result.append((left, right))
    return result

def min_subset_sum(arr):
    subsets = all_subset_partitions(arr)
    result = 9999
    for set in subsets:
        result = min(result, abs(sum(set[0])-sum(set[1])))
    return result

print(sorted(data))

print(min_subset_sum(data))


'''
[1,6,11,5]
for each element i, should include i in first subset or not?
trying to minimize difference of two sets
'''
def recursive_min_subset_sum(arr, n, current, total):

    if n == len(arr):
        return abs(total - current)

    return min(recursive_min_subset_sum(arr, n+1, current+arr[n], total-arr[n]),
               recursive_min_subset_sum(arr, n+1, current, total))

print(recursive_min_subset_sum(data, 0, 0, sum(data)))


'''
bottom up minimum subset sum:
dp[i][j] = true if sum J can be obtained by with arr up to (including) element I
dp[i][j] = max(dp[i-1][j], dp[

at the end, we need to do some extra math to find the minimum difference.
'''

def bu_min_subset_sum(arr, total):

    if not arr:
        return 0

    dp = [[False for _ in range(total+1)] for _ in range(len(arr)+1)]
    #abs difference with no total and no numbers in the left set is 0
    dp[0][0] = True

    for i in range(1, len(arr)+1):
        for j in range(1, total+1):
            if j - arr[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    #now we have the dp filled out, need to find the minimum sum difference
    #we are looking for the sum CLOSEST to sum(arr)//2
    #we know the PERFECT scenario is 2 equal sum subarrays, but the best we can do might be worse than that
    #so iterate from sum(arr)//2 down to zero, taking the first TRUE sum you find
    for x in range(sum(arr)//2, -1, -1):
        if dp[len(arr)][x]:
            return sum(arr) - x*2

    return 9999


print(bu_min_subset_sum(data, sum(data)))