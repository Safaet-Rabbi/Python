a = 0.0
M = []
T = input()
for _ in range(12):
    row = []
    for _ in range(12):
        value = float(input())
        row.append(value)
    M.append(row)

p = 0
r = 4
for z in range(1, 11):
    if z <= 5:
        for C in range(p + 1):
            a += M[z][C]
        p += 1
    elif z >= 6:
        for C in range(r + 1):
            a += M[z][C]
        r -= 1

if T[0] == 'S':
    print('%.1f' % a)
elif T[0] == 'M':
    a = a / 30.0
    print('%.1f' % a)