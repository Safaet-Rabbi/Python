def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    from collections import defaultdict
    
    freq = defaultdict(int)
    for num in a:
        freq[num] += 1
    
    inc = []  
    dec = []  
    
    for num in sorted(freq.keys()):
        if freq[num] > 2:
            print("NO")
            return
        elif freq[num] == 2:
            inc.append(num)
            dec.append(num)
        else:
            inc.append(num) 
    
    print("YES")
    print(len(inc))
    print(" ".join(map(str, inc)))
    print(len(dec))
    print(" ".join(map(str, sorted(dec, reverse=True))))

solve()
