def min_lights_to_turn_off(n, flats):
    lights_to_turn_off = 0
    i = 1
    while i < n - 1:
        if flats[i - 1] == 1 and flats[i + 1] == 1 and flats[i] == 0:
            flats[i + 1] = 0
            lights_to_turn_off += 1
            i += 2
        else:
            i += 1
            
    return lights_to_turn_off
n = int(input())
flats = list(map(int, input().split()))
print(min_lights_to_turn_off(n, flats))
