graph = dict()
n, m = map(int, input().split())
for _ in range(m):
    i, j = map(int, input().split())
    graph[i] = graph.get(i, []) + [j]
print(n)

for i in range(1, n + 1):
    print(len(graph.get(i, [])), *sorted(graph.get(i, [])))
