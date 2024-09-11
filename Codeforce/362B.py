def can_petya_reach_last_stair(n, m, dirty_stairs):
    if 1 in dirty_stairs or n in dirty_stairs:
        return "NO"
    
    dirty_stairs.sort()
    
    for i in range(m - 2):
        if dirty_stairs[i] + 1 == dirty_stairs[i + 1] and dirty_stairs[i + 1] + 1 == dirty_stairs[i + 2]:
            return "NO"
    
    return "YES"

n, m = map(int, input().split())
if m > 0:
    dirty_stairs = list(map(int, input().split()))
else:
    dirty_stairs = []
result = can_petya_reach_last_stair(n, m, dirty_stairs)
print(result)
