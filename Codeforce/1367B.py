t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    odd_count = 0
    even_count = 0
    for i in range(n):
        if i%2==0:
            if a[i]%2!=0:
                even_count+=1
        else:
            if a[i]%2!=1:
                odd_count+=1
    if even_count==odd_count:
        print(even_count)
    else:
        print(-1)
                