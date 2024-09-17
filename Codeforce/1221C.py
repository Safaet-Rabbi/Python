def max_perfect_teams(q, queries):
    results = []
    for c, m, x in queries:
        max_teams = min((c + m + x) // 3, min(c, m))
        results.append(max_teams)
    return results

q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

results = max_perfect_teams(q, queries)
for result in results:
    print(result)
