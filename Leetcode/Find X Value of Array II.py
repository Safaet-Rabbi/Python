from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        for i, v in enumerate(nums):
            p = size + i
            v %= k
            prod[p] = v
            cnt[p][v] = 1

        def pull(p):
            l = p << 1
            r = l | 1
            lp = prod[l]

            prod[p] = lp * prod[r] % k

            for x in range(k):
                cnt[p][x] = cnt[l][x]

            for x in range(k):
                if cnt[r][x]:
                    cnt[p][lp * x % k] += cnt[r][x]

        for p in range(size - 1, 0, -1):
            pull(p)

        def update(i, v):
            p = size + i
            v %= k
            prod[p] = v
            cnt[p] = [0] * k
            cnt[p][v] = 1

            p >>= 1
            while p:
                pull(p)
                p >>= 1

        def query(l, r):
            left_prod = 1
            left_cnt = [0] * k
            right_prod = 1
            right_cnt = [0] * k

            l += size
            r += size

            while l <= r:
                if l & 1:
                    lp = left_prod
                    for x in range(k):
                        left_cnt[lp * x % k] += cnt[l][x]
                    left_prod = left_prod * prod[l] % k
                    l += 1

                if not (r & 1):
                    rp = prod[r]
                    temp = [0] * k
                    for x in range(k):
                        temp[x] += cnt[r][x]
                        if right_cnt[x]:
                            temp[rp * x % k] += right_cnt[x]
                    right_cnt = temp
                    right_prod = rp * right_prod % k
                    r -= 1

                l >>= 1
                r >>= 1

            for x in range(k):
                left_cnt[left_prod * x % k] += right_cnt[x]

            return left_cnt

        ans = []

        for index, value, start, x in queries:
            update(index, value)
            ans.append(query(start, n - 1)[x])

        return ans