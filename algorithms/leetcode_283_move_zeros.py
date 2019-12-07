def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    lo = 0
    hi = 1
    while hi < len(nums):

        while lo < len(nums) - 1 and nums[lo] != 0:
            lo += 1
            hi += 1
        while hi < len(nums) and nums[hi] == 0:
            hi += 1

        if lo < len(nums) and hi < len(nums):
            nums[lo], nums[hi] = nums[hi], nums[lo]


data = [0,1,0,3,12]
moveZeroes(data)
print(data)