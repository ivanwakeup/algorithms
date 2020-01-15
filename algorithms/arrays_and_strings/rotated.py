def rotate(nums, k):
    for i in range(k):
        new_nums = [nums[-1]] + nums[:-1]
        nums = new_nums


print(rotate([1,2,3,4,5,6,7], 3))