def reconstruct_w(s, x):
    n = len(s)
    w = ['1'] * n

    for i in range(n):
        if s[i] == '0':
            if i - x >= 0:
                w[i - x] = '0'
            if i + x < n:
                w[i + x] = '0'

    for i in range(n):
        if s[i] == '1':
            if (i - x >= 0 and w[i - x] == '1') or (i + x < n and w[i + x] == '1'):
                continue
            return -1

    return ''.join(w)

t = int(input())
for _ in range(t):
    s = input().strip()
    x = int(input())
    print(reconstruct_w(s, x))
