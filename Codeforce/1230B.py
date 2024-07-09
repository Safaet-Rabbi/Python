def minimize_integer(n, k, s):
    s = list(s) 
    if n == 1 and k > 0:
        return '0'
    if k > 0:
        if s[0] != '1':
            s[0] = '1'
            k -= 1
    for i in range(1, n):
        if k <= 0:
            break
        if s[i] != '0':
            s[i] = '0'
            k -= 1
    return ''.join(s)
n, k = map(int, input().split())
s = input().strip()
result = minimize_integer(n, k, s)
print(result)
