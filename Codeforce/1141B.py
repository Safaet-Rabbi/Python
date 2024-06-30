def max_continuous_rest(n, a):
    a_extended = a + a    
    max_rest = 0
    current_rest = 0    
    for hour in a_extended:
        if hour == 1:
            current_rest += 1
            max_rest = max(max_rest, current_rest)
        else:
            current_rest = 0    
    return max_rest
n = int(input())
a = list(map(int, input().split()))
result = max_continuous_rest(n, a)
print(result)
