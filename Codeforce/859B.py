import math
def minimum_perimeter(N):
    min_perimeter = float('inf')
    for length in range(1, int(math.sqrt(N)) + 1):
        if N % length == 0:
            width = N // length
            perimeter = 2 * (length + width)
            min_perimeter = min(min_perimeter, perimeter)
        else:
            width = N // length + 1
            perimeter = 2 * (length + width)
            min_perimeter = min(min_perimeter, perimeter)
    
    return min_perimeter
N = int(input().strip())
result = minimum_perimeter(N)
print(result)
