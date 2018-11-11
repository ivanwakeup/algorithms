data = [2,2,3,5]

'''
if total isn't even, we cant have two equal sum subsets
otherwise treat this like a knapsack problem.
at each level of recursion, you can either include the current element in your pursuit of the target sum, or not.
you're just trying to find if ANY way exists to achieve your target sum.
'''
def equal_subset_sum(arr):
    total = sum(arr)
    if total % 2:
        return False
    target = total//2
    return has_target(arr, 0, target)

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


print("recursive subset sum is {}".format(equal_subset_sum(data)))


def bottom_up_ess(arr):

    total = sum(arr)
    if total % 2:
        return False
    target = total//2

