def min_abs_diff_between_classes(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        a = sorted(test_cases[i][1])
        results.append(abs(a[n] - a[n-1]))
    return results
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))
results = min_abs_diff_between_classes(t, test_cases)
for result in results:
    print(result)
