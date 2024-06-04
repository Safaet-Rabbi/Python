def minimum_road_width(n, h, friend_heights):

  total_width = 0
  for friend_height in friend_heights:
    if friend_height > h: 
      total_width += 2
    else:
      total_width += 1
  return total_width

n, h = map(int, input().split())
friend_heights = list(map(int, input().split()))

minimum_width = minimum_road_width(n, h, friend_heights)

print(minimum_width)
