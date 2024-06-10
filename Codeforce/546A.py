k,n,w = map(int,input().split())
TotalCost = k * (w*(w+1)) // 2
BananaBorrows = TotalCost - n
BananaNeeds = max(0,BananaBorrows)
print(BananaNeeds)