graph = {1: [2, 3, 4],
         2: [1, 4],
         3: [1],
         4: [1, 5, 6],
         5: [4, 6],
         6: [4, 5]}


def has_dfs_path(start, end):
    visited = []
    stack = [start]
    return has_dfs_path_r(start, end, stack, visited)


def has_dfs_path_r(start, end, stack, visited):
    if start == end:
        return True
    if stack:
        visited.append(start)
        to_visit = stack.pop(len(stack)-1)

        for neighbor in graph[to_visit]:
            if neighbor not in visited:
                stack.append(neighbor)
        return has_dfs_path_r(stack.pop(len(stack)-1), end, stack, visited)

    return False


print has_dfs_path(1, 6)
