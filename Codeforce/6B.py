n, m, c = input().split()
n, m = int(n), int(m)

office = [input().strip() for _ in range(n)]

unique_adjacent_desks = set()

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    for j in range(m):
        if office[i][j] == c:
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if office[ni][nj] != '.' and office[ni][nj] != c:
                        unique_adjacent_desks.add(office[ni][nj])

print(len(unique_adjacent_desks))
