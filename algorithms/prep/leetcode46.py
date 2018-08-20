def permute(nums):
    if not nums:
        return []
    result = []
    perms(nums, [], result)
    return result


def perms(nums, path, result):
    if not nums:
        result.append(path)
    for i in range(len(nums)):
        to_perm = nums[:i] + nums[i + 1:]
        perms(to_perm, path+[nums[i]], result)


print(permute([1,2,3]))