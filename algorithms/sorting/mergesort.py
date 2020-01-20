# def create_array(size=10, max=50):
#     from random import randint
#     return [randint(0,max) for _ in range(size)]
#
#
# def merge(a, b):
#     c = []
#
#     a_idx, b_idx = 0,0
#
#     while a_idx < len(a) and b_idx < len(b):
#         if a[a_idx] < b[b_idx]:
#             c.append(a[a_idx])
#             a_idx = a_idx + 1
#         else:
#             c.append(b[b_idx])
#             b_idx = b_idx + 1
#     if a_idx == len(a):
#         c.extend(b[b_idx:])
#     else:
#         c.extend(a[a_idx:])
#     return c
#
#
# def merge_sort(array):
#
#     if len(array) <= 1:
#         return array
#
#     left, right = merge_sort(array[:len(array)/2]), merge_sort(array[len(array)/2:])
#
#     return merge(left, right)
#
# a = create_array()
# print(merge_sort(a))




'''
lets write merge sort!

the key idea is the merge routine, which takes two sorted arrays and merges them together.

[1]
[2]

pretty straightforward with 2 pointers!

'''

def merge(a1, a2):
    i = 0
    j = 0
    res = []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            res.append(a1[i])
            i+=1
        else:
            res.append(a2[j])
            j+=1
    while i < len(a1):
        res.append(a1[i])
        i+=1
    while j < len(a2):
        res.append(a2[j])
        j+=1
    return res

def mergesort(arr, lo, hi):
    if lo == hi:
        return [arr[lo]]
    mid = (lo+hi)//2
    l = mergesort(arr, lo, mid)
    r = mergesort(arr, mid+1, hi)

    return merge(l, r)

data = [7,4,2,0,1,2,6,4]

print(mergesort(data, 0, len(data)-1))























































