def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = input().strip()
        a = []
        b = []
        a.append('1')
        b.append('1')
        split = False
        for i in range(1, n):
            if not split:
                if x[i] == '0':
                    a.append('0')
                    b.append('0')
                elif x[i] == '1':
                    a.append('1')
                    b.append('0')
                    split = True
                else:  
                    a.append('1')
                    b.append('1')
            else:
                a.append('0')
                b.append(x[i])
        
        print("".join(a))
        print("".join(b))

solve()
