import math
def min_segments(n):
    a = int(math.sqrt(n))
    b = math.ceil(n / a)
    return a + b
n = int(input())
print(min_segments(n))
