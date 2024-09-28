def sum_of_digits_written(n, m):
    cycle = []
    for i in range(1, 11):
        cycle.append((i * m) % 10)
    
    cycle_sum = sum(cycle)
    full_cycles = n // (m * 10)
    remaining_pages = (n // m) % 10
    
    total_sum = full_cycles * cycle_sum
    for i in range(remaining_pages):
        total_sum += cycle[i]
    
    return total_sum

q = int(input())
for _ in range(q):
    n, m = map(int, input().split())
    print(sum_of_digits_written(n, m))
