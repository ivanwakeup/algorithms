'''
easy solution:
find lowest N , K sized groups in the input roses
create max_sliding_window function that returns a result array which contains the max bloom day from each window size K
add each of these elements to a minheap, and pop N of them off the top -> the last one popped is the answer

return the max element found out of all the K groups
'''


def min_days_to_bloom(roses, k, n):
    '''

    :param roses: rose array to iterate
    :param k: the integer size of the "bouquet", how many roses which are adjacent to each other to form a group
    :param n: the total number of bouquets we need
    :return:
    '''
    #impossible to make n bouquets of k size if the input is too small
    if n*k > len(roses):
        return -1

    days = [x for x in max_sliding_window(roses, k)]

    #ensure we only select the best indexes from windows that aren't overlapping.
    #in other words, once we make our "best" bouquet we can't make another one from any flows in that window
    tmp = []
    for i in range(0, len(days), k):
        tmp.append(days[i])


    import heapq
    heapq.heapify(tmp)
    res = float('-inf')
    for _ in range(n):
        res = max(res, heapq.heappop(tmp))
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

roses = [1,2,4,9,3,3,1]
k = 2
n = 2
print(min_days_to_bloom(roses, k, n))