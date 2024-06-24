k2,k3,k5,k6 = map(int,input().strip().split())
num_256 = min(k2,k5,k6)
k2 -= num_256
num_32 = min(k2,k3)
total_sum = num_256*256 + num_32 * 32
print(total_sum)