from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = 0
        l = len(height) - 1
        s = 0  

        while r < l:
            t = min(height[r], height[l]) * (l - r)
            s = max(s, t)
            if height[r] < height[l]:
                r += 1
            else:
                l -= 1

        return s

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
print(solution.maxArea(height))  
