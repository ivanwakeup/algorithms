'''
Binary search is a search algorithm usually used on a sorted sequence to quickly find an element with a given value. In this problem we will evaluate how binary search performs on data that isn't necessarily sorted. An element is said to be binary searchable if, regardless of how the pivot is chosen the algorithm returns true. For example:

[2, 1, 3, 4, 6, 5] and target = 5, we cannot find 5. Because when the pivot is 4, we get element 6, then right pointer will move left, so we'll lose the opportunity to find target 5.
[2, 1, 3, 4, 5, 6] and target = 5, we can find 5. Because wherever we choose the pivots, we'll find target at last.
Given an unsorted array of n distinct integers, return the number of elements that are binary searchable.


intuitions:
1. the pivot can be chosen ANYWHERE. it doesn't have to be the mid. however, if an element is binary searchable
then it doesn't matter where you chose the pivot--if you follow the rules of binary search (reducing your search space
to either everything before or after the pivot) you should still be able to find that element eventually.

2. what this question is really asking is:

for every element, is every element to the left of it smaller and every element to the right of it greater? YES? then
it's binary searchable.

'''


'''
an n^2 approach would be:
for each element, compare it to every other element and ensure it abides by the rules
'''


def quadratic_is_searchable(arr):
    res = 0
    for i, n in enumerate(arr):
        can_do = True
        for j,n2 in enumerate(arr):
            if n2 == n:
                continue
            if j < i and n2 > n:
                can_do = False
            if j > i and n2 < n:
                can_do = False
        if can_do:
            res+=1
    return res


print(quadratic_is_searchable([2,1,3,4,6,5]))


'''
can we do better than n^2?
what if we created two arrays that stored what number each idx we're examining needs to be less than or greater than?

ex = [2,1,3,4,6,5]
lt = [1,3,4,5,5,inf]
gt = [-inf,2,2,3,4,6]

that works
'''

def is_searchable_linear(arr):
    lt = [float('inf')] * len(arr)
    gt = [float('-inf')] * len(arr)
    res = 0
    for i in range(1, len(arr)):
        lt[len(arr)-1-i] = min(lt[arr])
    for i, n in enumerate(arr):
