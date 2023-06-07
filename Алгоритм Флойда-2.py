N = int(input())

matrix = [[int(x) for x in input().split()] for i in range(N)]

for V in range(N):
    for from_v in range(N):
        for to_v in range(N):
            if matrix[from_v][to_v] != -1:
                matrix[from_v][to_v] = max(matrix[from_v][to_v], matrix[from_v][V] + matrix[V][to_v])

min = 99999
for from_v in range(N):
    for to_v in range(N):
        if matrix[from_v][to_v] < min and matrix[from_v][to_v] != -1:
            min = matrix[from_v][to_v]

print(min)