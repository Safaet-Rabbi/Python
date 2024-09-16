def min_compressions(n, m, songs):
    total_size = sum(a for a, b in songs)
    
    if total_size <= m:
        return 0
    
    savings = [(a - b) for a, b in songs]
    savings.sort(reverse=True)     
    compressions = 0
    for save in savings:
        total_size -= save
        compressions += 1
        if total_size <= m:
            return compressions
    
    return -1
n, m = map(int, input().split())
songs = []
for i in range(n):
    a, b = map(int, input().split())
    songs.append((a, b))
result = min_compressions(n, m, songs)
print(result)
