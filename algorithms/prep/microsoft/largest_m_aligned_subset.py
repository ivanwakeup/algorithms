'''
given an array of integers N and an integer M
find the largest M-aligned subset such that:
1. the distance between EVERY point in the subset is divisible by M
2. distance = abs(n[i]-n[j]) where i and j are two distinct entries in the input
example:
[-3, -2, 1, 0, 8, 7, 1]

the largest M-aligned subset is {-2, 1, 7, 1},
with distances between each entry and every other entry being divisible by 3


plan:
keep a list of subsets
iterate over input, and check each item i against each subset and each entry in that subset to determine if we can add it
if we can, add it and update our max_count. also add the current item to its own subset.


'''

'''
brute force method?
the runtime here is quite bad.
'''
def largest_m_aligned(arr, M):
    subsets = []
    res = 1
    for item in arr:
        nxt_se = []
        for se in subsets:
            can_add = True
            nxt = se.copy()
            for set_item in se:
                if abs(set_item - item) % M:
                    can_add = False
            if can_add:
                nxt.append(item)
                nxt_se.append(nxt)
            res = max(res, len(nxt))
        subsets.extend(nxt_se)
        subsets.append([item])
    return res

# print(
#     largest_m_aligned([-2, 1, 7, 1], 3)
# )


'''
MASSIVE OPTIMIZATION
'''


def largest_m_aligned_optimal(A, M):
    """ find the size of longest subset of A, in which any 2 elements' different is divisible by M """
    remainders = [0] * M
    max_size = 0
    for num in A:
        remainder = num % M
        remainders[remainder] += 1
        max_size = max(max_size, remainders[remainder])
    return max_size


print(largest_m_aligned_optimal([-3, -2, 1, 0, 8, 7, 1], 3))

