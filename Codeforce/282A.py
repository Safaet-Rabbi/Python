n=int(input())
statements = [input().strip() for _ in range(n)]
results = 0
for statement in statements:
    if '++' in statement:
        results+=1
    if '--' in statement:
        results-=1
print(results)