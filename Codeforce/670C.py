n = int(input())
scientists_languages = list(map(int, input().split()))
m = int(input())
audio_languages = list(map(int, input().split()))
subtitle_languages = list(map(int, input().split()))

audio_count = {}
subtitle_count = {}

for lang in scientists_languages:
    if lang in audio_count:
        audio_count[lang] += 1
    else:
        audio_count[lang] = 1
        
    if lang in subtitle_count:
        subtitle_count[lang] += 1
    else:
        subtitle_count[lang] = 1

best_movie = -1
max_pleased = -1
max_almost_satisfied = -1

for i in range(m):
    audio_lang = audio_languages[i]
    subtitle_lang = subtitle_languages[i]
    
    pleased = audio_count.get(audio_lang, 0)
    almost_satisfied = subtitle_count.get(subtitle_lang, 0)
    
    if pleased > max_pleased or (pleased == max_pleased and almost_satisfied > max_almost_satisfied):
        best_movie = i + 1
        max_pleased = pleased
        max_almost_satisfied = almost_satisfied

print(best_movie)
