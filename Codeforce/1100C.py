import math
n, r = map(int, input().split())
R = (r * math.sin(math.pi / n)) / (1 - math.sin(math.pi / n))
print(f"{R:.7f}")
