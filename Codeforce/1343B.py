def balanced_array(n):
    if (n // 2) % 2 != 0:
        return "NO"
    
    first_half = []
    second_half = []    
    for i in range(1, n // 2 + 1):
        first_half.append(2 * i)   
    for i in range(1, n // 2):
        second_half.append(2 * i - 1)
    
    second_half.append(sum(first_half) - sum(second_half))
    
    return "YES", first_half + second_half

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    result = balanced_array(n)
    if result == "NO":
        results.append("NO")
    else:
        results.append("YES")
        results.append(" ".join(map(str, result[1])))

for result in results:
    print(result)
