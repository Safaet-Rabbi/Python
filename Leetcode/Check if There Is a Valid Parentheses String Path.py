class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) & 1 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                cur = dp[i][j]
                add = 1 if grid[i][j] == '(' else -1

                if i:
                    for b in dp[i - 1][j]:
                        nb = b + add
                        if nb >= 0:
                            cur.add(nb)

                if j:
                    for b in dp[i][j - 1]:
                        nb = b + add
                        if nb >= 0:
                            cur.add(nb)

        return 0 in dp[-1][-1]