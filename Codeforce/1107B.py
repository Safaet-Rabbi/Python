def find_kth_number_with_digital_root(n, queries):
    results = []
    for k, x in queries:
        result = x + 9 * (k - 1)
        results.append(result)
    return results
n = int(input())
queries = []
for _ in range(n):
    k, x = map(int, input().split())
    queries.append((k, x))
results = find_kth_number_with_digital_root(n, queries)
for result in results:
    print(result)
