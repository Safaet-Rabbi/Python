def record_lecture(n, m, pairs, lecture):
    word_map = {}

    for a, b in pairs:
        if len(b) < len(a):
            word_map[a] = b
        else:
            word_map[a] = a
    
    result = []
    for word in lecture:
        result.append(word_map[word])
    
    return " ".join(result)

n, m = map(int, input().split())
pairs = []
print()
for _ in range(m):
    a, b = input().split()
    pairs.append((a, b))
lecture = input().split()
output = record_lecture(n, m, pairs, lecture)
print(output)
