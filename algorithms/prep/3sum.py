def threeSumBrute(nums):
    result = []
    sol = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    chkstr = " ".join(sorted(str(x) for x in [nums[i], nums[j], nums[k]]))
                    if not chkstr in sol:
                        sol.add(chkstr)
                        result.append([nums[i], nums[j], nums[k]])
    return result


print(threeSumBrute([-1, 0, 1, 2, -1, -4]))


def threeSumHm(nums):
    result = []
    hm = {}
    for num in nums:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    chkstr = " ".join(sorted(str(x) for x in [nums[i], nums[j], nums[k]]))
                    if not chkstr in sol:
                        sol.add(chkstr)
                        result.append([nums[i], nums[j], nums[k]])
    return result