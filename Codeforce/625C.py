n, k = map(int, input().split())
table = [[0] * n for _ in range(n)]
val = 1

for i in range(n):
    for j in range(k-1):
        table[i][j] = val
        val += 1

for i in range(n):
    for j in range(k-1, n):
        table[i][j] = val
        val += 1

column_sum = sum(table[i][k-1] for i in range(n))
print(column_sum)
for row in table:
    print(*row)
