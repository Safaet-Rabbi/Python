class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        curr = 0
        best = -1

        for right, v in enumerate(nums):
            curr += v

            while left <= right and curr > target:
                curr -= nums[left]
                left += 1

            if curr == target:
                best = max(best, right - left + 1)

        return n - best if best != -1 else -1