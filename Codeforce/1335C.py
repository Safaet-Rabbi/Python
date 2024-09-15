from collections import Counter

def max_team_size(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        
        skill_count = Counter(a)
        
        distinct_count = len(skill_count)
        
        max_frequency = max(skill_count.values())
        
        max_size = min(distinct_count, max_frequency)
        
        if distinct_count == max_frequency:
            results.append(max_size - 1)
        else:
            results.append(max_size)
    
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = max_team_size(t, test_cases)
for res in results:
    print(res)
