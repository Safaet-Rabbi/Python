def count_pairs(n, cake):
    row_counts = [0] * n
    col_counts = [0] * n  
    for i in range(n):
        for j in range(n):
            if cake[i][j] == 'C':
                row_counts[i] += 1
                col_counts[j] += 1
    
    row_pairs = sum((count * (count - 1)) // 2 for count in row_counts)
    
    col_pairs = sum((count * (count - 1)) // 2 for count in col_counts)
    
    return row_pairs + col_pairs
n = int(input().strip())
cake = [input().strip() for _ in range(n)]

print(count_pairs(n, cake))
