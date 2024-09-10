def count_bad_prices(prices):
    n = len(prices)
    bad_price_count = 0
    min_price = float('inf')
    
    for i in range(n - 1, -1, -1):
        if prices[i] > min_price:
            bad_price_count += 1
        min_price = min(min_price, prices[i])
    
    return bad_price_count

def process_input_data(test_cases):
    results = []
    
    for prices in test_cases:
        results.append(count_bad_prices(prices))
    
    return results

t = int(input().strip())
test_cases = []

for _ in range(t):
    n = int(input().strip())
    prices = list(map(int, input().strip().split()))
    test_cases.append(prices)

results = process_input_data(test_cases)

for result in results:
    print(result)
