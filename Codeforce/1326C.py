MOD = 998244353
def max_partition_value(n, k, p):
    max_sum = sum(sorted(p)[-k:])
    max_indices = sorted([i for i, x in enumerate(p) if x in set(sorted(p)[-k:])])
    ways = 1
    for i in range(1, len(max_indices)):
        ways = ways * (max_indices[i] - max_indices[i-1]) % MOD
    return max_sum, ways
n, k = map(int, input().split())
p = list(map(int, input().split()))
result = max_partition_value(n, k, p)
print(result[0], result[1])
