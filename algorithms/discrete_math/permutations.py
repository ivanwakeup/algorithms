def permute(s):

    out = []

    if len(s) == 1:
        out.append(s)

    for idx, letter in enumerate(s):
        for perm in permute(s[:idx] + s[idx+1:]):
            out.append(letter + perm)

    return out



print(permute("this"))


def compute_num_permutations_by_factorial(arr):
    if not arr:
        return 0
    n = len(arr)
    result = 1
    while n > 1:
        result *= n
        n-=1
    return result

print(compute_num_permutations_by_factorial([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))