def perform_the_combo(t, cases):
    results = []
    for n, m, s, p in cases:
        prefix_sum = [0] * n
        for pos in p:
            prefix_sum[0] += 1
            if pos < n:
                prefix_sum[pos] -= 1
        
        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]
        
        freq = [0] * 26
        for i in range(n):
            freq[ord(s[i]) - ord('a')] += prefix_sum[i] + 1
        
        results.append(" ".join(map(str, freq)))
    return results

t = int(input())
cases = []
for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()
    p = list(map(int, input().split()))
    cases.append((n, m, s, p))
for result in perform_the_combo(t, cases):
    print(result)
