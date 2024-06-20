t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    
    # Initialize the resulting string w
    w = ""
    
    # Construct w such that it is similar to all required substrings
    for i in range(n):
        w += s[i]
    
    print(w)
