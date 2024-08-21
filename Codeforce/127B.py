from collections import Counter
def max_frames(n, sticks):
    freq = Counter(sticks)
    pairs = 0
    for count in freq.values():
        pairs += count // 2
    return pairs // 2
n = int(input())
sticks = list(map(int, input().split()))
print(max_frames(n, sticks))
