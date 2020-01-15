'''
easy solution:
find lowest N , K sized groups in the input roses
create max_sliding_window function that returns a result arrays_and_strings which contains the max bloom day from each window size K
add each of these elements to a minheap, and pop N of them off the top -> the last one popped is the answer

return the max element found out of all the K groups
'''


def min_days_to_bloom(roses, k, n):
    '''

    :param roses: rose arrays_and_strings to iterate
    :param k: the integer size of the "bouquet", how many roses which are adjacent to each other to form a group
    :param n: the total number of bouquets we need
    :return:
    '''
    #impossible to make n bouquets of k size if the input is too small
    if n*k > len(roses):
        return -1

    days = [x for x in max_sliding_window(roses, k)]

    #ensure we only select the best indexes from windows that aren't overlapping.
    #we must keep track of both the item and the index to ensure its no overlap
    #when does it no overlap? when the second index is at least k away from the first

    from queue import PriorityQueue
    pq = PriorityQueue()
    for i in range(len(days)):
        pq.put((days[i], [i, days[i]]))

    it = pq.get()[1][1]
    res = it
    valid = n - 1

    while not pq.empty() and valid:
        item = pq.get()
        if abs(item[1][0]-k)<=0:
            res = max(res, item[1][1])
            valid-=1
    return res



from collections import deque


def max_sliding_window(arr, k):
    d = deque()
    res = []
    for i, n in enumerate(arr):
        while d and arr[d[-1]] < n:
            d.pop()
        d.append(i)
        if d[0] <= i - k:
            d.popleft()
        if i >= k - 1:
            res.append(arr[d[0]])
    return res

roses = [5,1,1,1,2,3,2,1,1]
k = 2
n = 2
print(min_days_to_bloom(roses, k, n))