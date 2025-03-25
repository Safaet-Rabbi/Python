class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        counts = [[a, 'a'], [b, 'b'], [c, 'c']]

        while True:
            counts.sort(reverse=True)
            added = False

            for i in range(3):
                if counts[i][0] <= 0:
                    continue
                if len(res) >= 2 and res[-1] == res[-2] == counts[i][1]:
                    continue
                res.append(counts[i][1])
                counts[i][0] -= 1
                added = True
                break

            if not added:
                break

        return ''.join(res)
