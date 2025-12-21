import heapq

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('Z', 6)],
    'E': [('C', 10), ('D', 2), ('Z', 3)],
    'Z': [('D', 6), ('E', 3)]
}

def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        dist, v = heapq.heappop(heap)
        if dist > distances[v]:
            continue
        for neigh, w in graph[v]:
            new_dist = dist + w
            if new_dist < distances[neigh]:
                distances[neigh] = new_dist
                heapq.heappush(heap, (new_dist, neigh))

    return distances

#приклад
start = 'A'
shortest = dijkstra(graph, start)
print(shortest)