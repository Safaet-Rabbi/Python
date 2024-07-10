def can_transform(s, t):
    return bool(set(s) & set(t))
q = int(input())
results = []
for _ in range(q):
    s = input().strip()
    t = input().strip()
    if can_transform(s, t):
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result)
