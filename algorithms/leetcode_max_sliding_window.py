from collections import deque

'''
maintain an invariant that we always have the max element of the current window at the front of the deque. simply remove that element
if it falls outside of the window. if we encounter a new greatest element, remove everything that comes from the queue before it which is smaller--
this is what maintains the invariant.


'''
def maxSlidingWindow(nums, k):
    res = []
    q = deque()
    for i, n in enumerate(nums):
        #once we encounter something larger than what we last appended, it MUST be a candidate for the max.
        while q and nums[q[-1]] < n:
            q.pop()
        q.append(i)
        if q[0] <= i-k:
            q.popleft()
        if i >= k - 1:
            res.append(nums[q[0]])
    return res

data = [1,3,-1,-3,5,3,6,7]
k=3

print(maxSlidingWindow(data, k))