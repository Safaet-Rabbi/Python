def max_possible_price(t, queries):
    results = []
    for query in queries:
        n, k = query[0]
        prices = query[1]
        min_possible = prices[0] - k
        max_possible = prices[0] + k
        for price in prices[1:]:
            min_possible = max(min_possible, price - k)
            max_possible = min(max_possible, price + k)

            if min_possible > max_possible:
                results.append(-1)
                break
        else:
            results.append(max_possible)
    
    return results
t = int(input())
queries = []
for _ in range(t):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    queries.append(((n, k), prices))
results = max_possible_price(t, queries)
for result in results:
    print(result)
