def min_paving_cost(t, test_cases):
    results = []
    for case in test_cases:
        n, m, x, y, grid = case
        total_cost = 0    
        for row in grid:
            i = 0
            while i < m:
                if row[i] == '.':
                    if i + 1 < m and row[i + 1] == '.':
                        if y < 2 * x:
                            total_cost += y
                            i += 2
                        else:
                            total_cost += x
                            i += 1
                    else:
                        total_cost += x
                        i += 1
                else:
                    i += 1
        
        results.append(total_cost)
    return results
t = int(input())
test_cases = []
for _ in range(t):
    n, m, x, y = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    test_cases.append((n, m, x, y, grid))
results = min_paving_cost(t, test_cases)
for result in results:
    print(result)
