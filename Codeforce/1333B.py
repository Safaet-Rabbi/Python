def can_transform(n, a, b):
    has_pos = has_neg = False
    for i in range(n):
        if b[i] > a[i] and not has_pos:
            return "NO"
        if b[i] < a[i] and not has_neg:
            return "NO"
        if a[i] == 1:
            has_pos = True
        if a[i] == -1:
            has_neg = True
    return "YES"
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    results.append(can_transform(n, a, b))
print("\n".join(results))
