def find_z(x, y):
    n = len(x)
    z = []
    for i in range(n):
        if y[i] > x[i]:
            return -1
        z.append(y[i])
    return "".join(z)
x = input().strip()
y = input().strip()
result = find_z(x, y)
print(result)
