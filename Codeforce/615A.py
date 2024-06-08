def can_light_all_bulbs(n, m, button_bulbs):
    turned_on_bulbs = set()
    
    for bulbs in button_bulbs:
        for bulb in bulbs:
            turned_on_bulbs.add(bulb)
    
    for bulb in range(1, m + 1):
        if bulb not in turned_on_bulbs:
            return "NO"
    
    return "YES"
n, m = map(int, input().split())
button_bulbs = []
for _ in range(n):
    input_data = list(map(int, input().split()))
    x = input_data[0] 
    bulbs = input_data[1:x+1]  
    button_bulbs.append(bulbs)
result = can_light_all_bulbs(n, m, button_bulbs)
print(result)
