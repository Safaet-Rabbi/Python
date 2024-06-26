def beat_dragon(x,n,m):
    while n > 0 and x > 20:
        x = x//2 + 10
        n -= 1
    if x <= m * 10:
        return "YES"
    return "NO"
t = int(input().strip())
results = []
for _ in range(t):
    x,n,m = map(int,input().strip().split())
    results.append(beat_dragon(x,n,m))
for result in results:
    print(result)