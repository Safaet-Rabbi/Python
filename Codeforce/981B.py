def max_total_income(n, chemforces, m, topchemist):
    chemforces_dict = {a: x for a, x in chemforces}
    topchemist_dict = {b: y for b, y in topchemist}    
    total_income = 0    
    for a, x in chemforces:
        if a in topchemist_dict:
            total_income += max(x, topchemist_dict[a])
            topchemist_dict.pop(a)
        else:
            total_income += x
    for b, y in topchemist_dict.items():
        total_income += y
    
    return total_income
n = int(input().strip())
chemforces = [tuple(map(int, input().strip().split())) for _ in range(n)]
m = int(input().strip())
topchemist = [tuple(map(int, input().strip().split())) for _ in range(m)]
result = max_total_income(n, chemforces, m, topchemist)
print(result)
