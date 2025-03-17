import heapq

def prims_algorithm(V, edges):
    # Create an adjacency list
    graph = {i: [] for i in range(V)}
    for u, v, w in edges:
        graph[u].append((w, v))  # (weight, destination)
        graph[v].append((w, u))  # Undirected graph

    # Min-Heap to store the next minimum edge
    min_heap = [(0, 0)]  # (weight, start node)
    visited = set()
    mst_weight = 0  # Total weight of MST

    while len(visited) < V:
        weight, u = heapq.heappop(min_heap)

        # If the node is already visited, continue
        if u in visited:
            continue

        # Add to MST
        visited.add(u)
        mst_weight += weight

        # Add all connected edges to the heap
        for edge in graph[u]:
            if edge[1] not in visited:
                heapq.heappush(min_heap, edge)

    return mst_weight

# Test case
V = 5
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

print("Total weight of MST:", prims_algorithm(V, edges))
