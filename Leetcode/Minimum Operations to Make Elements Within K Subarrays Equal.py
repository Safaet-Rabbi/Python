class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        arr = [bisect_left(vals, v) + 1 for v in nums]

        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(bit, i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            res = 0
            while i:
                res += bit[i]
                i -= i & -i
            return res

        def kth(q):
            idx = 0
            bit_mask = 1 << (m.bit_length() - 1)

            while bit_mask:
                nxt = idx + bit_mask
                if nxt <= m and cnt[nxt] < q:
                    idx = nxt
                    q -= cnt[nxt]
                bit_mask >>= 1

            return idx + 1

        costs = []
        window_sum = 0

        for i, v in enumerate(nums):
            p = arr[i]
            update(cnt, p, 1)
            update(sm, p, v)
            window_sum += v

            if i >= x:
                old = nums[i - x]
                p = arr[i - x]
                update(cnt, p, -1)
                update(sm, p, -old)
                window_sum -= old

            if i >= x - 1:
                mid = kth((x + 1) // 2)
                median = vals[mid - 1]

                left_count = query(cnt, mid)
                left_sum = query(sm, mid)

                left_cost = median * left_count - left_sum
                right_cost = window_sum - left_sum - median * (x - left_count)

                costs.append(left_cost + right_cost)

        inf = float('inf')
        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        dp[0] = [0] * (n + 1)

        for t in range(1, k + 1):
            for i in range(t * x, n + 1):
                dp[t][i] = min(
                    dp[t][i - 1],
                    dp[t - 1][i - x] + costs[i - x]
                )

        return dp[k][n]