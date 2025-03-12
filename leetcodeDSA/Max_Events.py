import heapq

def maxEvents(events):
    events.sort()  # Sort events by start day
    min_heap = []  # Min heap to store event end days
    day, count, i, n = 0, 0, 0, len(events)

    while i < n or min_heap:
        # Move to the next available day
        if not min_heap:
            day = events[i][0]

        # Add all events that start on or before `day`
        while i < n and events[i][0] <= day:
            heapq.heappush(min_heap, events[i][1])  # Push event end day
            i += 1

        # Remove past events
        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)

        # Attend the event with the **earliest ending day**
        if min_heap:
            heapq.heappop(min_heap)
            count += 1  # One event attended
            day += 1  # Move to next day

    return count

print(maxEvents([[1,2],[2,3],[3,4],[1,2]]))  # Output: 4
print(maxEvents([[1,2],[2,3],[3,4],[1,2],[3,4]]))  # Output: 4
print(maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))  # Output: 4
