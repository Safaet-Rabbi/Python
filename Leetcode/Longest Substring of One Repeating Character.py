from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        size = 4 * n

        lc = [""] * size
        rc = [""] * size
        pref = [0] * size
        suff = [0] * size
        best = [0] * size
        length = [0] * size

        def pull(p):
            l, r = p * 2, p * 2 + 1
            length[p] = length[l] + length[r]
            lc[p] = lc[l]
            rc[p] = rc[r]

            pref[p] = pref[l]
            suff[p] = suff[r]
            best[p] = max(best[l], best[r])

            if rc[l] == lc[r]:
                best[p] = max(best[p], suff[l] + pref[r])

                if pref[l] == length[l]:
                    pref[p] = length[l] + pref[r]

                if suff[r] == length[r]:
                    suff[p] = length[r] + suff[l]

        def build(p, l, r):
            length[p] = r - l + 1

            if l == r:
                lc[p] = rc[p] = s[l]
                pref[p] = suff[p] = best[p] = 1
                return

            m = (l + r) // 2
            build(p * 2, l, m)
            build(p * 2 + 1, m + 1, r)
            pull(p)

        def update(p, l, r, idx, c):
            if l == r:
                lc[p] = rc[p] = c
                return

            m = (l + r) // 2

            if idx <= m:
                update(p * 2, l, m, idx, c)
            else:
                update(p * 2 + 1, m + 1, r, idx, c)

            pull(p)

        build(1, 0, n - 1)

        ans = []

        for c, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, c)
            ans.append(best[1])

        return ans