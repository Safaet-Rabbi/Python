count=0
n=int(input())
for _ in range(n):
    p,v,t =map(int,input().split())
    if p+v+t>=2:
        count+=1
        print(count)