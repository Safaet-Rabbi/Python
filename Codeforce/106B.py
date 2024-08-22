n = int(input())
laptops = []

for i in range(n):
    speed, ram, hdd, cost = map(int, input().split())
    laptops.append((speed, ram, hdd, cost, i + 1))

non_outdated = []
for i in range(n):
    is_outdated = False
    for j in range(n):
        if i != j and (laptops[i][0] < laptops[j][0] and laptops[i][1] < laptops[j][1] and laptops[i][2] < laptops[j][2]):
            is_outdated = True
            break
    if not is_outdated:
        non_outdated.append(laptops[i])
non_outdated.sort(key=lambda x: x[3]) 
print(non_outdated[0][4])
