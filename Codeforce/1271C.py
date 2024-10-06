def shawarma_tent(n, sx, sy, students):
    north_count = 0
    south_count = 0
    east_count = 0
    west_count = 0
    
    for x, y in students:
        if y > sy:
            north_count += 1
        if y < sy:
            south_count += 1
        if x > sx:
            east_count += 1
        if x < sx:
            west_count += 1
    
    max_count = max(north_count, south_count, east_count, west_count)
    
    if max_count == north_count:
        return max_count, sx, sy + 1
    elif max_count == south_count:
        return max_count, sx, sy - 1
    elif max_count == east_count:
        return max_count, sx + 1, sy
    else:
        return max_count, sx - 1, sy

n, sx, sy = map(int, input().split())
students = [tuple(map(int, input().split())) for _ in range(n)]
c, px, py = shawarma_tent(n, sx, sy, students)
print(c)
print(px, py)
