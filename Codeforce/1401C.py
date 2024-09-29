import math

def can_sort_with_gcd(n, arr):
    min_val = min(arr)
    sorted_arr = sorted(arr)
    swappable_elements = [x for x in arr if x % min_val == 0]
    for i in range(n):
        if arr[i] != sorted_arr[i] and arr[i] not in swappable_elements:
            return "NO"
    
    return "YES"

t = int(input().strip()) 
results = []
for _ in range(t):
    n = int(input().strip()) 
    arr = list(map(int, input().strip().split()))  
    results.append(can_sort_with_gcd(n, arr))
print("\n".join(results))
