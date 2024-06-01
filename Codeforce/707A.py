def is_color(n, m , matrix):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] in ['C','M','Y']:
                return False
    
    return True


n,m = map(int, input().split())
matrix = []
for _ in range(n):
    row = input().split()
    matrix.append(row)
result = "#Black&White" if is_color(n,m,matrix) else "#Color"
print(result)
