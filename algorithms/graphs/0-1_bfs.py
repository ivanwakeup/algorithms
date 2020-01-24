'''
0-1 bfs can be used like dijkstras algorithm to find the shortest path in a graph

the catch is that we can only have 0 or 1 for the edge weights

this lets us use a DEQUE instead of a priority queue or heap for keeping track of what paths
we need to visit next
'''