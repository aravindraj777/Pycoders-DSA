import heapq
from collections import defaultdict

def findCheapestPrice(n, flights, src, dst, k):
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))

    # Min Heap: (cost, current city, stops remaining)
    min_heap = [(0, src, k + 1)]

    # Dijkstra's Algorithm with Stop Constraints
    while min_heap:
        cost, city, stops = heapq.heappop(min_heap)

        # If reached destination, return cost
        if city == dst:
            return cost

        # If there are stops remaining, explore neighbors
        if stops > 0:
            for neighbor, price in graph[city]:
                heapq.heappush(min_heap, (cost + price, neighbor, stops - 1))

    return -1  # No valid route

print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,3,100],[0,2,500]], 0, 3, 1))  # Output: 200
print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))  # Output: 200
print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))  # Output: 500
