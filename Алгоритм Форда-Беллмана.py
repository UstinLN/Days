N, M = map(int, input().split())
graph = []
dist = dict()

for i in range(M):
    from_V, to_V, weight = map(int, input().split())
    graph.append((from_V - 1, to_V - 1, weight))

start = 0
dist = [float('inf')] * N
dist[start] = 0

for i in range(N - 1):
    for from_V, to_V, weight in graph:
        if dist[from_V] + weight < dist[to_V]:
            dist[to_V] = dist[from_V] + weight

for i in range(N):
    if dist[i] == float('inf'):
        dist[i] = 30000

print(*dist)