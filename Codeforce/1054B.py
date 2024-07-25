def can_make_non_ascending(n, rectangles):
    prev_max_height = float('inf')
    
    for i in range(n):
        w, h = rectangles[i]
        heights = [w, h] if w <= h else [h, w]
        if heights[1] <= prev_max_height:
            prev_max_height = heights[1]
        elif heights[0] <= prev_max_height:
            prev_max_height = heights[0]
        else:
            return "NO"
    
    return "YES"
n = int(input())
rectangles = []
for _ in range(n):
    w, h = map(int, input().split())
    rectangles.append((w, h))
result = can_make_non_ascending(n, rectangles)
print(result)
