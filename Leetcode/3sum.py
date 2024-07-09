class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        if n < 3 or nums[0] > 0:
            return []
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, n - 1
            target = -nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i], nums[l], nums[r]])
                    lastLeft, lastRight = nums[l], nums[r]
                    while l < n and nums[l] == lastLeft:
                        l += 1
                    while r >= 0 and nums[r] == lastRight:
                        r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
        return res