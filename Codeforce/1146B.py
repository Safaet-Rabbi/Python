def find_s(t):
    n = len(t)
    a_count = t.count('a')
    potential_s_len = (n + a_count) // 2
    
    if potential_s_len * 2 - a_count != n:
        return ":("
    
    s = t[:potential_s_len]
    s_prime = ''.join([char for char in s if char != 'a'])
    
    if s + s_prime == t:
        return s
    else:
        return ":("
t = input()
print(find_s(t))
