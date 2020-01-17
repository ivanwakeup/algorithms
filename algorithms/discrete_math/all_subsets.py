# DFS recursively
def subsets1(nums):
    res = []
    dfs(nums, 0, [], res)
    return res


def dfs(nums, index, current, res):
    res.append(current)
    for i in range(index, len(nums)):
        next = current + [nums[i]]
        dfs(nums, i + 1, next, res)


print(subsets1([2,1,3]))
