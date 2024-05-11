from collections import defaultdict

def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

    return result

# Example usage
graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [0, 3, 4]
graph[2] = [0, 4]
graph[3] = [1, 4]
graph[4] = [1, 2, 3]

print("Depth-First Search:")
dfs_result = dfs(graph, 0)
print(dfs_result)

## Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph. On the worst case DFS will visit all vertices and edges.
