def maximum_sum(k2, k3, k5, k6):
    num_256 = min(k2, k5, k6)
    k2 -= num_256   
    num_32 = min(k2, k3)
    
    total_sum = num_256 * 256 + num_32 * 32   
    return total_sum
k2, k3, k5, k6 = map(int, input().split())
print(maximum_sum(k2, k3, k5, k6))
