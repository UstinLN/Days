N = int(input())

matrix = [[int(x) for x in input().split()]for i in range(N)]

for V in range(N):
    for p in range(N):
        for q in range(N):
            matrix[p][q] = min(matrix[p][q], matrix[p][V] + matrix[V][q])

max = 0
for p in range(N):
    for q in range(N):
        if matrix[p][q] > max:
            max = matrix[p][q]

print(max)