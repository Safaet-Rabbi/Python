def min_prefix_to_delete(n, a):
    i = n - 1
    
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
        
    while i > 0 and a[i - 1] <= a[i]:
        i -= 1
    
    return i

t = int(input()) 
for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))  
    print(min_prefix_to_delete(n, a))
