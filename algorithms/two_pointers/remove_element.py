def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    if len(nums) == 1:
        return 1 if nums[0] != val else 0

    lo = 0
    hi = 1
    while hi < len(nums):

        while lo < len(nums) and nums[lo] != val:
            lo += 1
            hi += 1
        while hi < len(nums) and nums[hi] == val:
            hi += 1

        # now we have nums to be swapped
        if lo < len(nums) and hi < len(nums):
            nums[lo], nums[hi] = nums[hi], nums[lo]

    return max(0, lo)


assert removeElement([3,2,2,3], 3) == 2