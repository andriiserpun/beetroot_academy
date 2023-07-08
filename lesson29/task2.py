def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('inf')] * V for _ in range(V)]
    next = [[None] * V for _ in range(V)]
    for u in range(V):
        for v in range(V):
            dist[u][v] = graph[u][v]
            if u != v and graph[u][v] != float('inf'):
                next[u][v] = v
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]
    return dist, next
graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]
distances, next_vertices = floyd_warshall(graph)
for i in range(len(graph)):
    for j in range(len(graph)):
        print(f"Shortest distance from vertex {i} to vertex {j}: {distances[i][j]}")