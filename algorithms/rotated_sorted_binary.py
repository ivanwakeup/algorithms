class Solution:
    def search(self, nums, target):

        def do_find(nums, target, cur):
            if not nums:
                return -1
            mid = len(nums) // 2
            if nums[mid] == target:
                return cur + mid
            elif nums[mid] < target:
                if mid + 1 < len(nums) and nums[mid + 1] <= target:
                    return do_find(nums[mid+1:], target, mid+1)
                if mid - 1 >= 0 and nums[mid - 1] >= target:
                    return do_find(nums[:mid], target, 0)
            else :
                if mid - 1 >= 0 and nums[mid-1] >= target:
                    return do_find(nums[:mid], target, cur)
                if mid + 1 < len(nums) and nums[mid + 1] <= target:
                    return do_find(nums[mid + 1:], target, mid + 1)

        return do_find(nums, target, 0)




sol = Solution()

print(sol.search([3,5,1], 3))
