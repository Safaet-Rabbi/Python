from collections import Counter
def can_transform(s, t, p):
    it = iter(t)
    if not all(c in it for c in s):
        return "NO"  
    count_s = Counter(s)
    count_t = Counter(t)
    count_p = Counter(p)    
    for char in count_t:
        if count_t[char] > count_s[char] + count_p[char]:
            return "NO"   
    return "YES"
q = int(input())
for _ in range(q):
    s = input()
    t = input()
    p = input()
    print(can_transform(s, t, p))
