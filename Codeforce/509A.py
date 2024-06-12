def max_in_table(n):
    table = [[0] * n for _ in range(n)]

    for i in range(n):
        table[i][0] = 1
        table[0][i] = 1
        

    for i in range(1,n):
        for j in range(1,n):
            table[i][j] = table[i][j-1] + table[i-1][j]

    return table[n-1][n-1]

n = int(input().strip())
print(max_in_table(n))