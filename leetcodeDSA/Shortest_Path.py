import heapq


def dijkstra(n, edges, src):
    # Step 1: Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))

    # Step 2: Initialize distance array and priority queue
    dist = {i: float('inf') for i in range(n)}
    dist[src] = 0
    pq = [(0, src)]  # (distance, node)

    # Step 3: Process nodes in priority queue
    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > dist[node]:  # Ignore outdated distances
            continue

        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor]:  # Found a shorter path
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    # Step 4: Convert unreachable nodes (-1) and return result
    return [dist[i] if dist[i] != float('inf') else -1 for i in range(n)]


# Example usage
n = 5
edges = [[0, 1, 10], [0, 4, 3], [1, 2, 2], [2, 3, 5], [4, 1, 4], [4, 2, 8]]
src = 0
print(dijkstra(n, edges, src))  # Output: [0, 7, 9, 14, 3]
