def insert(queue, item):
    pos = 0

    count, val = item

    rem = 0

    size = len(queue)

    while pos < size:

        if queue[pos][0] >= val:
            rem += 1

        if rem > count:
            break

        pos += 1

    if pos == size:
        queue.append([val, count])
    else:
        queue.insert(pos, [val, count])

import heapq
def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    items = []
    for height, k in people:
        items.append((k, height))

    queue = []

    heapq.heapify(items)

    while len(items) != 0:
        item = heapq.heappop(items)

        insert(queue, item)

    return queue


input = [[7,0], [4,4], [7,1], [6,1], [5,2], [5,0]]

output = reconstructQueue(input)
print(output)

'''
2i + 1 <= i
2i + 2 <= i

'''
def validate_min_heap(arr, i):
    if i >= len(arr) or len(arr) == 1:
        return True
    left_v = True
    right_v = True
    if 2*i + 1 < len(arr):
        left_v = arr[i] <= arr[2*i + 1] and validate_min_heap(arr, 2*i + 1)
    if 2*i + 2 < len(arr):
        right_v = arr[i] <= arr[2*i + 2] and validate_min_heap(arr, 2*i + 2)

    return left_v and right_v

res = validate_min_heap([(0, 7), (1, 6), (0, 5), (4, 4), (2, 5), (1, 7)], 0)
print(res)
