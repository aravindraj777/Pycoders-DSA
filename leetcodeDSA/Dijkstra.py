import heapq

def dijkstra(V, edges, source):
    # Create adjacency list
    graph = {i: [] for i in range(V)}
    for u, v, w in edges:
        graph[u].append((w, v))  # (weight, destination)

    # Min-Heap (distance, node)
    min_heap = [(0, source)]
    distances = {i: float('inf') for i in range(V)}
    distances[source] = 0

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)

        # If the popped distance is greater than the recorded one, skip
        if current_dist > distances[u]:
            continue

        # Explore neighbors
        for weight, v in graph[u]:
            distance = current_dist + weight

            # Update if a shorter distance is found
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(min_heap, (distance, v))

    # Convert dictionary to a sorted list of distances
    return [distances[i] for i in range(V)]

# Test case
V = 5
edges = [
    (0, 1, 10),
    (0, 4, 3),
    (1, 2, 2),
    (1, 4, 4),
    (2, 3, 9),
    (3, 2, 7),
    (4, 1, 1),
    (4, 2, 8),
    (4, 3, 2)
]
source = 0

print("Shortest distances from source", source, ":", dijkstra(V, edges, source))
