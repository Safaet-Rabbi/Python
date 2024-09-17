def find_shortest_dominated_subarray():
    T = int(input())  
    for _ in range(T):
        n = int(input())  
        a = list(map(int, input().split())) 
        last_seen = {}
        min_length = float('inf') 
        for i in range(n):
            if a[i] in last_seen:
             
                subarray_length = i - last_seen[a[i]] + 1
                min_length = min(min_length, subarray_length)
            
            last_seen[a[i]] = i
        
        if min_length == float('inf'):
            print(-1)
        else:
            print(min_length)

find_shortest_dominated_subarray()
