def minimum_shots(n, durabilities):
    cans = [(durabilities[i], i + 1) for i in range(n)]    
    cans.sort(reverse=True, key=lambda x: x[0])
    
    total_shots = 0
    order = []
    for x in range(n):
        ai, index = cans[x]
        total_shots += ai * x + 1
        order.append(index)
    
    return total_shots, order
n = int(input())
durabilities = list(map(int, input().split()))
total_shots, order = minimum_shots(n, durabilities)
print(total_shots)
print(" ".join(map(str, order)))
