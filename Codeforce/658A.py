def contest_winner(n, c, p, t):
    limak_time = 0
    limak_score = 0
    for i in range(n):
        limak_time += t[i]
        limak_score += max(0, p[i] - c * limak_time)
    
    radewoosh_time = 0
    radewoosh_score = 0
    for i in range(n-1, -1, -1):
        radewoosh_time += t[i]
        radewoosh_score += max(0, p[i] - c * radewoosh_time)
    
    if limak_score > radewoosh_score:
        return "Limak"
    elif radewoosh_score > limak_score:
        return "Radewoosh"
    else:
        return "Tie"

n, c = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))
result = contest_winner(n, c, p, t)
print(result)
