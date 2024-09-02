def max_wealthy_people(n, x, a):
    a.sort(reverse=True)
    total_sum = 0
    count = 0
    
    for i in range(n):
        total_sum += a[i]
        if total_sum >= x * (i + 1):
            count = i + 1
        else:
            break
    
    return count

T = int(input())
results = []

for _ in range(T):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    results.append(max_wealthy_people(n, x, a))

for result in results:
    print(result)
