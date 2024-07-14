class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = 0
        lp = 0
        res = len(nums)+1
        for i in range(len(nums)):
            n += nums[i]
            while n >= target:
                res = min(i-lp+1, res)
                n -= nums[lp]
                lp += 1
        return 0 if res == len(nums) + 1 else res