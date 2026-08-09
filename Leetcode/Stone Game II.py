class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @cache
        def f(i, M):
            if i+2*M >= n:
                return suffix[i]

            outcomes = []
            for X in range(1,M+1):
                outcomes.append(f(i+X,M))
            for X in range(M+1,2*M+1):
                outcomes.append(f(i+X,X))
            return suffix[i]-min(outcomes)
        return f(0,1)