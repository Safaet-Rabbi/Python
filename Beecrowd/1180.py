n=int(input())
x=list(map(int,input().split()))
smallest=x[0]
position=0
for i in range(1, n):
    if x[i]<smallest:
        smallest=x[i]
        position=i
	    

print("Menor valor:",smallest)
print("Posicao:",position)