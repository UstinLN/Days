count_vertex, start, end = map(int, input().split())
dist = dict()
visited = dict()
graph = dict()
for key in range(1, count_vertex + 1):
    row = [int(x) for x in input().split()]
    dist[key] = (float('inf'), [key])
    visited[key] = 0
    neighbours = []
    for index, value in enumerate(row):
        if value >= 0:
            neighbours.append((index + 1, value))
    graph[key] = neighbours

queue = [start]
dist[start] = (0, [start])
while queue:
    vertex_to = queue.pop(0)
    if visited[vertex_to]:
        continue
    visited[vertex_to] = 1
    for node in graph[vertex_to]:
        vertex_from = node[0]
        weight = node[1]
        new_cost = weight + dist[vertex_to][0]
        if new_cost < dist[vertex_from][0]:
            dist[vertex_from] = (new_cost, dist[vertex_to][1] + [vertex_from])
            queue.append(vertex_from)
            visited[vertex_from] = 0


if dist[end][0] == float('inf'):
    print(-1)
else:
    print(*dist[end][1])