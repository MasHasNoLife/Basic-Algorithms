from collections import defaultdict, deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

# Example usage
graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [0, 3, 4]
graph[2] = [0, 4]
graph[3] = [1, 4]
graph[4] = [1, 2, 3]

print("Breadth-First Search:")
bfs_result = bfs(graph, 0)
print(bfs_result)

## Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph. In the worst case, BFS visits all vertices and edges.
