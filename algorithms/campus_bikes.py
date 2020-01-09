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


def campus_bikes(workers, bikes):
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


workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]

#print(campus_bikes(workers, bikes))



