def permute(arr):
    result = []
    if len(arr) == 1:
        return arr

    for i in range(len(arr)):
        for perm in permute(arr[:i] + arr[i+1:]):
            result.append([arr[i]] + perm)

    return result



print(permute([1,2,3]))