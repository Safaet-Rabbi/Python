def min_moves(t,TestCases):
    results = []
    for i in range(t):
        n,a,b = TestCases[i]
        minA = min(a)
        minB = min(b)
        total_moves = 0
        for j in range(n):
            delta_a = a[j] - minA
            delta_b = b[j] - minB
            moves = max(delta_a,delta_b)
            total_moves+= moves
        results.append(total_moves)
        
    return results
t = int(input().strip())
TestCases = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int,input().strip().split()))          
    b = list(map(int,input().strip().split())) 
    TestCases.append((n,a,b))

results = min_moves(t,TestCases)
for result in results:
    print(result)         

