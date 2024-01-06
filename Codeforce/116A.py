n=int(input())
capacity=0
current_passenger = 0
for _ in range(n):
    a,b=map(int,input().split())
    current_passenger -=a
    current_passenger +=b
    capacity=max(capacity,current_passenger)
    
print(capacity)