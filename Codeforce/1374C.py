def minimum_moves_to_RBS(s):
    balance = 0
    max_imbalance = 0
    
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        if balance < 0:
            max_imbalance = max(max_imbalance, -balance)
    
    return max_imbalance

t = int(input()) 
for _ in range(t):
    n = int(input())
    s = input() 
    
    print(minimum_moves_to_RBS(s))
