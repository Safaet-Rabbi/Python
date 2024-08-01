def find_min_replacements(n, m, s, t):
    min_replacements = float('inf')
    best_positions = []

    for i in range(m - n + 1):
        current_replacements = 0
        current_positions = []
        for j in range(n):
            if s[j] != t[i + j]:
                current_replacements += 1
                current_positions.append(j + 1)
        
        if current_replacements < min_replacements:
            min_replacements = current_replacements
            best_positions = current_positions

    return min_replacements, best_positions

n, m = map(int, input().split())
s = input().strip()
t = input().strip()

min_replacements, best_positions = find_min_replacements(n, m, s, t)

print(min_replacements)
print(" ".join(map(str, best_positions)))
