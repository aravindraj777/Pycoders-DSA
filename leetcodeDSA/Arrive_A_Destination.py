import heapq

MOD = 10**9 + 7

def countPaths(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v, time in edges:
        graph[u].append((v, time))
        graph[v].append((u, time))

    min_time = [float('inf')] * n
    ways = [0] * n
    min_time[0] = 0
    ways[0] = 1

    pq = [(0, 0)]  # (time, node)

    while pq:
        time, node = heapq.heappop(pq)

        if time > min_time[node]:
            continue

        for neighbor, t in graph[node]:
            new_time = time + t

            if new_time < min_time[neighbor]:
                min_time[neighbor] = new_time
                ways[neighbor] = ways[node]
                heapq.heappush(pq, (new_time, neighbor))

            elif new_time == min_time[neighbor]:
                ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

    return ways[n - 1]

#test
n = 7
edges = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[5,4,6],[4,3,2]]
print(countPaths(n, edges))  # Output: 4
