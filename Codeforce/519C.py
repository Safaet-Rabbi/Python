def max_teams(n, m):
    return min(min(n, m), (n + m) // 3)
n, m = map(int, input().split())
print(max_teams(n, m))
