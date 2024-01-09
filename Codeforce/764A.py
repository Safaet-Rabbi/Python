import math
m,n,z=map(int,input().split())
lcm= (m*n)//math.gcd(n,m)

artists=z//lcm
print(artists)