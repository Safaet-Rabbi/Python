class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        a = sorted((r, l, w, i) for i, (l, r, w) in enumerate(intervals))
        rights = [x[0] for x in a]
        n = len(a)

        prev = [bisect_left(rights, l) for r, l, w, i in a]
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            r, l, w, idx = a[i - 1]
            p = prev[i - 1]

            for k in range(1, 5):
                best = dp[i - 1][k]
                score, seq = dp[p][k - 1]
                cand = (score + w, tuple(sorted(seq + (idx,))))

                if cand[0] > best[0] or (cand[0] == best[0] and cand[1] < best[1]):
                    best = cand

                dp[i][k] = best

        ans = ()
        score = -1

        for k in range(1, 5):
            s, seq = dp[n][k]
            if s > score or (s == score and seq < ans):
                score, ans = s, seq

        return list(ans)