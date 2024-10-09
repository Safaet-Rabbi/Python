def can_form_array(n, k, a):
    powers_used = {}
    
    for num in a:
        power = 0
        while num > 0:
            remainder = num % k
            if remainder > 1:
                return False
            if remainder == 1:
                if power in powers_used:
                    return False
                powers_used[power] = True
            num //= k
            power += 1
    
    return True

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if can_form_array(n, k, a):
        print("YES")
    else:
        print("NO")
