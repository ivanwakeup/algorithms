graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'E', 'H'],
    'D': ['A', 'E'],
    'E': ['D', 'C'],
    'H': ['C', 'F'],
    'F': ['H']
}

def get_dfs_array(graph, start_node, result, visited):

    result.append(start_node)
    visited.add(start_node)
    for node in graph[start_node]:
        if node not in visited:
            get_dfs_array(graph, node, result, visited)

    return result


def get_bfs_array(graph, start_node, result, visited):

    queue = [start_node]
    visited.add(start_node)

    while queue:
        start = queue.pop(0)
        result.append(start)
        for node in graph[start]:
            if node not in visited:
                queue.append(node)
                visited.add(node)
    return result


print(get_dfs_array(graph, 'A', [], set()))

print(get_bfs_array(graph, 'A', [], set()))

