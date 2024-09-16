def max_teams(n, weights):
    max_pairs = 0
    
    for s in range(2, 2 * n + 1):
        freq = [0] * (n + 1)  
        for w in weights:
            freq[w] += 1
        
        pairs = 0
        for w in range(1, (s // 2) + 1):
            if s - w > n:
                continue
            if w == s - w:  
                pairs += freq[w] // 2
            else:
                pairs += min(freq[w], freq[s - w])
        
        max_pairs = max(max_pairs, pairs)
    
    return max_pairs
t = int(input())  
for _ in range(t):
    n = int(input()) 
    weights = list(map(int, input().split())) 
    print(max_teams(n, weights))
