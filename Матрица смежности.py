N = int(input())
matrix = [[int(x) for x in input().split()]for i in range(N)]
graph = dict()
for i in range(1, N + 1):
    graph[i] = []

m = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            m += 1
            graph[i + 1] += [j + 1]
print(N, m)
for i in range(1, N + 1):
    if len(graph[i]) > 0:
        for neighbour in graph[i]:
            print(i, neighbour)