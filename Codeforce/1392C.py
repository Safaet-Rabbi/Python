def min_operations(t, test_cases):
    results = []
    
    for case in test_cases:
        n, arr = case
        operations = 0
        
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                operations += arr[i - 1] - arr[i]
        
        results.append(operations)
    
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))
results = min_operations(t, test_cases)
for result in results:
    print(result)
