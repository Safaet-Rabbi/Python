t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    p = []
    seen = set()
    
    for num in a:
        if num not in seen:
            p.append(num)
            seen.add(num)
    
    print(' '.join(map(str, p)))
