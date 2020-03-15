class Solution:
    def canPartition(self, nums):
        if sum(nums) % 2 != 0:
            return False

        def find(nums, i, curr, tgt, memo):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return False
            if nums[i] + curr > tgt:
                return False
            if nums[i] + curr == tgt:
                return True
            has = find(nums, i + 1, curr + nums[i], tgt, memo)
            doesnt_has = find(nums, i + 1, curr, tgt, memo)
            ans = max(has, doesnt_has)
            memo[i] = ans
            return ans

        return find(nums, 0, 0, sum(nums) // 2, {})


sol = Solution()

print(
    sol.canPartition([1,5,11,5])
)