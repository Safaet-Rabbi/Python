n = int(input())
full_cycle = n // 3
remainder = n % 3
turns = full_cycle * 2
if remainder > 0 :
    turns+=1 
print(turns)