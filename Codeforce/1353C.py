def solve():
    t = int(input()) 
    results = []
    
    for _ in range(t):
        n = int(input())
        m = (n - 1) // 2
        result = 8 * m * (m + 1) * (2 * m + 1) // 6
        results.append(result)
    
    print("\n".join(map(str, results)))

solve()
