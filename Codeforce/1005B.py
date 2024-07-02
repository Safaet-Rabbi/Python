def equal_strings(s,t):
    i,j = len(s) - 1, len(t) - 1
    while i>=0 and j>=0 and s[i]==t[j]:
        i -= 1
        j -= 1
    moves = (i+1) + (j+1)
    return moves
s = input().strip()
t = input().strip()
result = equal_strings(s,t)
print(result) 