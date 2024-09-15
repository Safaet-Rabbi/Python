def frog_jumps():
    t = int(input()) 
    results = []
    
    for _ in range(t):
        s = input()  
        max_distance = 0
        prev_position = 0  
        
        for i in range(len(s)):
            if s[i] == 'L':
                continue
            max_distance = max(max_distance, i + 1 - prev_position)
            prev_position = i + 1
        
        max_distance = max(max_distance, len(s) + 1 - prev_position)
        
        results.append(max_distance)
    
    for result in results:
        print(result)

frog_jumps()
