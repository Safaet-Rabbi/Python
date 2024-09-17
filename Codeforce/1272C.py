def solve():
    n, k = map(int, input().split())
    s = input()
    allowed = set(input().split())
    
    count = 0
    current_length = 0
    
    for char in s:
        if char in allowed:
            current_length += 1
        else:
            count += current_length * (current_length + 1) // 2
            current_length = 0
    
    count += current_length * (current_length + 1) // 2
    
    print(count)

solve()
