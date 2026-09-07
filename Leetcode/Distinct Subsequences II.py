class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        total = 0

        for c in s:
            i = ord(c) - 97
            new = (total + 1) % MOD
            total = (total + new - dp[i]) % MOD
            dp[i] = new

        return total