'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''


class Solution:
    def subsetsWithDup(self, nums):
        res = []
        seen = set()
        def dfs(nums, i, path, fs):
            if fs in seen:
                return
            seen.add(fs)
            res.append(path)
            if i >= len(nums):
                return
            for j in range(i, len(nums)):
                nxt = path + [nums[j]]
                nxt.sort()
                dfs(nums, j + 1, nxt, frozenset([str(nxt)]))

        dfs(nums, 0, [], frozenset())
        return res


sol = Solution()

print(sol.subsetsWithDup([1,2,2]))