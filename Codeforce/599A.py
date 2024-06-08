def minimum_distance(d1, d2, d3):
    route1 = d1 + d3 + d2
    route2 = 2 * (d1 + d2)
    route3 = 2 * (d1 + d3)
    route4 = 2 * (d2 + d3)
    
    return min(route1, route2, route3, route4)
d1, d2, d3 = map(int, input().split())
print(minimum_distance(d1, d2, d3))
