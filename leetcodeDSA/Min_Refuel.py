import heapq

def minRefuelStops(target, startFuel, stations):
    max_heap = []  # Max heap to store available fuel at stations
    stations.append([target, 0])  # Treat target as a final "station"

    fuel = startFuel
    stops = 0
    prev_position = 0

    for position, gas in stations:
        fuel -= (position - prev_position)  # Use fuel to reach this station

        # If we run out of fuel, refuel using the max available fuel from past stations
        while fuel < 0 and max_heap:
            fuel += -heapq.heappop(max_heap)  # Get max fuel available
            stops += 1  # Increase refueling stops

        if fuel < 0:
            return -1  # Impossible to reach target

        heapq.heappush(max_heap, -gas)  # Store fuel as negative (max heap behavior)
        prev_position = position  # Move to next station

    return stops


print(minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]]))  # Output: 2
print(minRefuelStops(100, 50, [[25,25],[50,50]]))  # Output: 1
print(minRefuelStops(200, 50, [[50,50],[100,50],[150,50]]))  # Output: 3
