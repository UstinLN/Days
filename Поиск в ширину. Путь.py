N = int(input())
queue = list()
visited = set()
dist = [None] * N
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}
for i in range(1, N + 1):
    queue[i] = []
    visited[i] = False
    matrix_row = [int(x) for x in input().split()]
    for index, value in enumerate(matrix_row):
        if value == 1:
            queue[i].append(index + 1)


def bfs(visited, graph, start):
    visited.add(start)
    queue.append(start)
    dist[start] = 0
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                dist[neighbour] = dist[start] + 1


bfs(visited, graph, 'A')
print(dist['D'])