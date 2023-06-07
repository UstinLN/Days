def p(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])

n = int(input())
g = [[0] * n for _ in range(n)]
for i in range(n):
    row = [int(x) for x in input().split()]
    if len(row) > 1:
        for neighboard in row[1:]:
            g[i][neighboard - 1] = 1
print(n)
p(g)