n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 2, 0, -1):
    for j in range(m - 2, 0, -1):
        if a[i][j] == 0:
            a[i][j] = min(a[i + 1][j], a[i][j + 1]) - 1

for i in range(n):
    for j in range(m - 1):
        if a[i][j] >= a[i][j + 1]:
            print(-1)
            exit()

for j in range(m):
    for i in range(n - 1):
        if a[i][j] >= a[i + 1][j]:
            print(-1)
            exit()

print(sum(sum(row) for row in a))
