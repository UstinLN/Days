N = int(input())

matrix = [[int(x) for x in input().split()]for i in range(N)]

for V in range(N):
    for from_V in range(N):
        for to_V in range(N):
            matrix[from_V][to_V] = min(matrix[from_V][to_V], matrix[from_V][V] + matrix[V][to_V])

for from_V in range(N):
    for to_V in range(N):
        print(matrix[from_V][to_V], end="  ")
    print(" ")