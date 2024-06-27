def max_spent_burles(t, test_cases):
    results = []
    for s in test_cases:
        total_spent = 0
        while s >= 10:
            spend = s - (s % 10)
            cashback = spend // 10
            total_spent += spend
            s = s - spend + cashback
        total_spent += s  
        results.append(total_spent)
    return results
t = int(input())
test_cases = [int(input()) for _ in range(t)]
results = max_spent_burles(t, test_cases)
for result in results:
    print(result)
