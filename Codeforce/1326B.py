def reconstruct_array(n, b):
    a = [0] * n
    x = 0
    for i in range(n):
        a[i] = b[i] + x
        x = max(x, a[i])
    return a
n = int(input())
b = list(map(int, input().split()))
a = reconstruct_array(n, b)
print(" ".join(map(str, a)))
