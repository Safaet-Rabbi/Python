from typing import List
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
        ans = [0] * n
        start = 0
        curr_max = nums[0]
        for i in range(n - 1):
            curr_max = max(curr_max, nums[i])

            if curr_max <= suffix_min[i + 1]:
                comp_max = max(nums[start:i + 1])

                for j in range(start, i + 1):
                    ans[j] = comp_max

                start = i + 1
                curr_max = nums[start]

        comp_max = max(nums[start:])

        for j in range(start, n):
            ans[j] = comp_max

        return ans