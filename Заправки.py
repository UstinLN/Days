n = int(input())
graph = dict()
visited = dict()
dist = dict()
cost = [0] + list(map(int, input().split()))
m = int(input())

for k in range(1, n + 1):
    graph[k] = []
    dist[k] = float('inf')
    visited[k] = 0
for p in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

queue = [1]
dist[1] = 0
while queue:
    vertex_to = queue.pop(0)
    if visited[vertex_to]:
        continue
    visited[vertex_to] = 1
    for vertex_from in graph[vertex_to]:
        new_cost = cost[vertex_to] + dist[vertex_to]
        if new_cost < dist[vertex_from]:
            dist[vertex_from] = new_cost
            queue.append(vertex_from)
            visited[vertex_from] = 0
if dist[n] == float('inf'):
    print('-1')
else:
    print(dist[n])
