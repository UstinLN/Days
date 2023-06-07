N, M = map(int, input().split())
graph = dict()
for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    i, j = map(int, input().split())
    graph[i] += [j]
    graph[j] += [i]

print(*list(map(lambda x: len(x), graph.values())))