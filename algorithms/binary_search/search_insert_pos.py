def searchInsert(nums, target):
    return recurse(nums, target, 0)


def recurse(nums, target, idx):
    mid = len(nums) // 2
    if nums[mid] == target:
        return idx + mid
    if len(nums) == 1 and target >= nums[0]:
        return idx + 1
    elif len(nums) == 1 and target < nums[0]:
        return idx

    if target < nums[mid]:
        return recurse(nums[:mid], target, idx)
    else:
        return recurse(nums[mid:], target, mid + idx)


print(searchInsert([1,3,5,6], 7))