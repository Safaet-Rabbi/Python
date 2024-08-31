def min_taxis(n, groups):
    count1 = groups.count(1)
    count2 = groups.count(2)
    count3 = groups.count(3)
    count4 = groups.count(4)    
    taxis = count4    
    pairs = min(count3, count1)
    taxis += pairs
    count3 -= pairs
    count1 -= pairs    
    taxis += count3    
    taxis += count2 // 2
    
    if count2 % 2 == 1:
        taxis += 1
        count1 -= min(count1, 2)  
    
    if count1 > 0:
        taxis += (count1 + 3) // 4  
    
    return taxis
n = int(input())
groups = list(map(int, input().split()))
print(min_taxis(n, groups))
