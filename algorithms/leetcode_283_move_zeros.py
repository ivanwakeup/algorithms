def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    lo = 0
    hi = 1
    while lo < len(nums) and hi < len(nums):

        while lo < len(nums) - 1 and nums[lo] != 0:
            lo += 1

        while hi < len(nums) - 1 and nums[hi] == 0:
            hi += 1

        nums[lo], nums[hi] = nums[hi], nums[lo]
        hi+=1


data = [0,1,0,3,12]
moveZeroes(data)
print(data)