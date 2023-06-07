n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

oriented = False
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            oriented = True
        if i == j and matrix[i][j] != 0:
            oriented = False
            break
    if not oriented:
        break

if oriented:
    print("YES")
else:
    print("NO")

