def threeSum(nums):
    result = set()
    hm = set(nums)
    i = 0
    j = 1
    while j < len(nums):
        s1 = nums[i]
        s2 = nums[j]
        s3 = ~(s1 + s2) + 1
        if s3 in hm:
            asc = sorted([s1,s2,s3])
            tup = tuple(asc)
            result.add(tup)
        i+=1
        j+=1
    return result

print(threeSum([-1, 0, 1, 2, -1, -4]))