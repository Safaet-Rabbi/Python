def can_partition_into_similar_pairs(n, a):
    a.sort()

    odd_count = sum(1 for x in a if x % 2 == 1)
    even_count = n - odd_count  

    if odd_count % 2 == 0 and even_count % 2 == 0:
        return True

    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) == 1:
            return True

    return False

t = int(input())  
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split())) 
    
    if can_partition_into_similar_pairs(n, a):
        print("YES")
    else:
        print("NO")
