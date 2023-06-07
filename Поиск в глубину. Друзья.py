def dfs(start):
    global count
    if visited[start]:
        return 0
    visited[start] = True
    count += 1
    for neighbours in neighbour[start]:
        dfs(neighbours)


count_vertex, start = map(int, input().split())
neighbour = dict()
visited = dict()
count = 0
for i in range(1, count_vertex + 1):
    neighbour[i] = []
    visited[i] = False
    matrix_row = [int(x) for x in input().split()]
    for index, value in enumerate(matrix_row):
        if value == 1:
            neighbour[i].append(index + 1)

dfs(start)
print(count - 1)