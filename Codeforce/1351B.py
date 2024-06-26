def is_square_possible(a1, b1, a2, b2):
    if (a1 == a2 and b1 + b2 == a1) or \
       (a1 == b2 and b1 + a2 == a1) or \
       (b1 == a2 and a1 + b2 == b1) or \
       (b1 == b2 and a1 + a2 == b1):
        return "YES"
    else:
        return "NO"

t = int(input().strip())
results = []
for _ in range(t):
    a1, b1 = map(int, input().strip().split())
    a2, b2 = map(int, input().strip().split())
    results.append(is_square_possible(a1, b1, a2, b2))

for result in results:
    print(result)
