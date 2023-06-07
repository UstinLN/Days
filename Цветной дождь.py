N = int(input())
graph = dict()
for i in range(1, N + 1):
    graph[i] = []
for i in range(N):
    for j, values in enumerate(input().split()):
        if values == '1':
            graph[i + 1] += [j + 1]
input()
colors_N = [0] + [int(x) for x in input().split()]
count = 0
for key in range(1, N + 1):
    for value in graph[key]:
        if colors_N[key] != colors_N[value]:
            count += 1
print(count // 2)