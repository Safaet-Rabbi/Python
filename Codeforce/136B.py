def to_ternary(n):
    ternary = []
    if n == 0:
        return [0]
    while n > 0:
        ternary.append(n % 3)
        n //= 3
    return ternary[::-1]

def from_ternary(ternary):
    n = 0
    for digit in ternary:
        n = n * 3 + digit
    return n

def find_b(a, c):
    ternary_a = to_ternary(a)
    ternary_c = to_ternary(c)
    
    while len(ternary_a) < len(ternary_c):
        ternary_a.insert(0, 0)
    while len(ternary_c) < len(ternary_a):
        ternary_c.insert(0, 0)
    
    b_digits = [(c_i - a_i) % 3 for a_i, c_i in zip(ternary_a, ternary_c)]
    return from_ternary(b_digits)

a, c = map(int, input().strip().split())

b = find_b(a, c)

print(b)
