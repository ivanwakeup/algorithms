'''
this is interesting. so, it works because we maintain the invariant that deque[0] always contains the max element in the current window.
how do we do that?
1. while the element we're considering is greater than what we last appended to the deque, pop it off.
    obviously, this will leave us in a situation where deque[0] contains the greatest element!

2. now, we just need to make sure we remove the greatest element once it no longer falls within the current window.
    we do this by checking if the index of the greatest element is > i-k (if it is, keep it because its still in the current window)


lastly, only add the element thats at nums[deque[0]] if we've formed a window of size k!

other notes:
we need to store the INDEX not the VALUE in the deque, because it helps us keep track of if element we're considering is still inside the current window.

what is the current window? i-k+1


INTUITIONS:
1. the deque helps us maintain a data structure that can remove and add items from BOTH ends in constant time.
'''
from collections import deque


def maxSlidingWindow(nums, k):
    d = deque()
    res = []

    for i, n in enumerate(nums):
        # if we find the next largest element, get rid of everything before it
        while d and nums[d[-1]] < n:
            d.pop()
        # d[0] now contains the highest value
        d.append(i)
        # if d[0] is outside of the window get rid of it
        if i - k == d[0]:
            d.popleft()
        # append to result if we've made at least k size window
        if i >= k - 1:
            res.append(nums[d[0]])
    return res
