t = int(input()) 
for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))    
    max_sum = 0
    max_val = a[0]   
    for i in range(1, n):
        if (a[i] > 0 and a[i-1] > 0) or (a[i] < 0 and a[i-1] < 0):
            max_val = max(max_val, a[i])
        else:
            max_sum += max_val
            max_val = a[i]   
    max_sum += max_val 
    print(max_sum)
