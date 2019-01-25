'''
we are given a graph representing modules and their dependencies
given a dependency input, we want to find a valid build order for being able to build that dependency
'''

graph = {
    "A" : ["B"],
    "B" : ["C", "D"],
    "C" : ["F", "E"],
    "D" : ["C", "E"],
    "E": [],
    "F": []
}

'''
approach:
do a dfs, once we find a module that has no dependencies we can add it to our result
maintain a processed set, make sure we only add or process modules that aren't already in that set
if no neighbors, add to result

else:
dfs(for each neighbor)


'''
visited = set()
result = []
def find_build_order(start, graph):
    visited.add(start)
    if not graph[start]:
        result.append(start)
        return
    for neigh in graph[start]:
        if neigh not in visited:
            find_build_order(neigh, graph)
    result.append(start)


find_build_order("D", graph)

print(result)