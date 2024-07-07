class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x) [::-1]
        og = str(x)
        if og==rev:
            return True
        else: return False
sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))