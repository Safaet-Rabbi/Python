n = int(input())
s = input().strip()

s = s.lower()
UniqueChars = set(s)
if len(UniqueChars) >= 26:
    print("YES")
else: 
    print("NO")