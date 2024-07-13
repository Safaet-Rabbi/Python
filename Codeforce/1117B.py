def max_happiness(n, m, k, a):
    a.sort(reverse=True)
    max1 = a[0]
    max2 = a[1]
    full_pattern_size = k + 1
    full_patterns = m // full_pattern_size
    remaining_uses = m % full_pattern_size
    total_happiness = full_patterns * (k * max1 + max2)
    total_happiness += remaining_uses * max1 
    return total_happiness
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
print(max_happiness(n, m, k, a))
