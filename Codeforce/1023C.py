def find_bracket_subsequence(n, k, s):
    open_needed = k // 2 
    close_needed = k // 2
    result = []

    for char in s:
        if char == '(' and open_needed > 0:
            result.append('(')
            open_needed -= 1
        elif char == ')' and close_needed > 0 and open_needed < k // 2:
            result.append(')')
            close_needed -= 1
        
        if len(result) == k:
            break

    return ''.join(result)
n, k = map(int, input().split())
s = input()
result = find_bracket_subsequence(n, k, s)
print(result)
