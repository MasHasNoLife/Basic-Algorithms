import heapq
from collections import defaultdict

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage
graph = defaultdict(dict)
graph[0] = {1: 4, 2: 1}
graph[1] = {0: 4, 2: 3, 3: 2, 4: 3}
graph[2] = {0: 1, 1: 3, 5: 1}
graph[3] = {1: 2, 4: 4, 5: 5}
graph[4] = {1: 3, 3: 4, 5: 1}
graph[5] = {2: 1, 3: 5, 4: 1}

print("Dijkstra's Algorithm:")
distances = dijkstra(graph, 0)
for vertex, distance in distances.items():
    print(f"Vertex {vertex}: Distance = {distance}")

## Time Complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph. This is because every vertex is enqueued and dequeued at most once in the priority queue, which takes O(log V) time, and the total number of operations on the adjacency list is O(E).
