class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or, count = 0, 0
        n = len(nums)
        
        def dfs(index, curr_or):
            nonlocal max_or, count
            if index == n:
                if curr_or > max_or:
                    max_or = curr_or
                    count = 1
                elif curr_or == max_or:
                    count += 1
                return
            dfs(index + 1, curr_or | nums[index])
            dfs(index + 1, curr_or)
        
        dfs(0, 0)
        return count
