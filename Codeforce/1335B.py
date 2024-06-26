def str(n,a,b):
    base_pattern = ''.join(chr(97 + i) for i in range(b))
    repeated_pattern = (base_pattern * ((n//b)+1))[:n]
    return repeated_pattern
t = int(input().strip())
results = []
for _ in range(t):
    n,a,b = map(int,input().strip().split())
    results.append(str(n,a,b))
for result in results:
    print(result)
