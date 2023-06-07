graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}
n = 5
queue = list()
visited = set()
dist = [None] * n


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