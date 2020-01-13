'''
On a campus represented as a 2D grid, there are Nworkers and Mbikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.
Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike)
pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike)
 pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that,
 we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points p1and p2is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|. Return a vector ansof length N,
where ans[i]is the index (0-indexed) of the bike that the i-th worker is assigned to.
examples


Input:
workers = [[0,0],[2,1]],
bikes = [[1,2],[3,3]]
Output:
[1,0]
Explanation:

Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].



ideas:
for each bike, calculate the manhattan distance from that bike to each worker. as we do that, keep track of the index
of the best bike->person distance we've seen so far, and only overwrite that if we get a better distance as we traverse

once we end the traversal for determining each of the distances, set an EMPTY marker in the person array to denote we used that one


algorithm:
    res = []
    for each bike:
        best = float('inf')
        for each person:
            if not empty person:
                dist = get_manhat(bike, person)
                best = min(best, dist)


problem with above^
this doesnt really FOLLOW the algorithm. we first need to calculate the manhattan distance, start with the shortest distances
and for each set of distances that are equal, assign the bike to the lowest index worker
if a worker has multiple bikes at the same distance from them, THEN assign the lowest index bike
'''


def campus_bikes_incorrect(workers, bikes):
    res = []
    for bike in bikes:
        local_best = 0
        best = float('inf')
        for i, worker in enumerate(workers):
            if not worker:
                continue
            dist = manhattan(bike, worker)
            if dist < best:
                local_best = i
                best = dist
        res.append(local_best)
        workers[local_best] = None
    return res


def manhattan(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


workers = [[0,0],[0,1],[1,1],[2,0]]
bikes = [[1,0],[1,2],[2,2],[2,1],[3,3]]

#print(campus_bikes(workers, bikes))

'''
ok, let's make a better one!

so, we are using the observation that lexicographic comparions are used in python sorting, and that sorting is stable.
this also holds true for something like a PriorityQueue. So, we can:
1. create all worker,bike pairs and store (distance, worker_idx, bike_idx) in a priority queue
2. keep a set to track what workers and bikes have been assigned. if we pop off the queue and worker and bike are already taken,
skip em
3. we are done once len(res) == len(workers)


runtime analysis:
0(n*m) to build the heap, need to construct each manhattan pair
0(n*mlogm) to analyze heap and pick bikes
0(nm) extra space
'''
from queue import PriorityQueue
def campus_bikes(workers, bikes):
    res = [None] * len(workers)
    pq = PriorityQueue()
    for i, bike in enumerate(bikes):
        for j, worker in enumerate(workers):
            dist = manhattan(bike, worker)
            pq.put((dist, j, i))
    seen = set()
    while pq and len(seen)//2 != len(workers):
        item = pq.get()
        wkey = "w"+str(item[1])
        bkey = "b"+str(item[2])
        if wkey in seen:
            continue
        elif bkey in seen:
            continue
        res[item[1]] = item[2]
        seen.update({wkey, bkey})
    return res

print(campus_bikes(workers, bikes))

import heapq
def assignBikes(workers, bikes):
    distances = []  # distances[worker] is tuple of (distance, worker, bike) for each bike
    for i, (x, y) in enumerate(workers):
        distances.append([])
        for j, (x_b, y_b) in enumerate(bikes):
            distance = abs(x - x_b) + abs(y - y_b)
            distances[-1].append((distance, i, j))
        distances[-1].sort(reverse=True)  # reverse so we can pop the smallest distance

    result = [None] * len(workers)
    used_bikes = set()
    queue = [distances[i].pop() for i in range(len(workers))]  # smallest distance for each worker
    heapq.heapify(queue)

    while len(used_bikes) < len(workers):
        _, worker, bike = heapq.heappop(queue)
        if bike not in used_bikes:
            result[worker] = bike
            used_bikes.add(bike)
        else:
            heapq.heappush(queue, distances[worker].pop())  # bike used, add next closest bike

    return result

print(assignBikes(workers, bikes))