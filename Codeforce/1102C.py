n, x, y = map(int, input().split())
a = list(map(int, input().split()))
if x > y:
    print(n)
else:
    count = sum(1 for durability in a if durability <= x)
    print((count + 1) // 2)
