def solve():
    t = int(input().strip())
    results = []

    for _ in range(t):
        n = int(input().strip())
        strengths = list(map(int, input().strip().split()))
        
        strengths.sort()
        
        min_diff = float('inf')
        for i in range(1, n):
            min_diff = min(min_diff, strengths[i] - strengths[i - 1])
        
        results.append(min_diff)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()
