n = int(input())
matrix = [[int(x) for x in input().split()]for i in range(n)]
answer = []
count = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == matrix[j][i] == 1:
            count += 1
    answer += str(count)
    count = 0
print(*answer)