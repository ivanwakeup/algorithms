data = [1,5,11,5]


def equal_subset_sum(arr):
    total = sum(arr)
    if total % 2:
        return False
    target = total//2
    return has_target(arr, 0, target, {})

def has_target(arr, i, target):
    if target == 0:
        return True
    includes = False

    if i >= len(arr):
        return False

    next_target = target - arr[i]
    if next_target >= 0:
        includes = has_target(arr, i+1, next_target)
    not_includes = has_target(arr, i+1, target)
    result = max(includes, not_includes)
    return result


def bottom_up_ess(arr):

    total = sum(arr)
    if total % 2:
        return False
    target = total//2

