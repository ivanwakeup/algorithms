def insert(self, queue, item):
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


def reconstructQueue(self, people):
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

        self.insert(queue, item)

    return queue


input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
