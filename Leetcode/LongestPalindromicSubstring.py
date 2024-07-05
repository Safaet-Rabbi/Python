class Solution:
    def longestpalindrome(self, s):
     def expand_around(s, left, right):
        while left>=0 and right < len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return left + 1,right - 1
     start = 0
     end = 0
     for i in range(len(s)):
        left1,right1 = expand_around(s,i,i)
        left2,right2 = expand_around(s,i,i+1)

        if right1 - left1 > end - start:
            start,end = left1,right1
        if right2 - left2 > end - start:
            start,end = left2,right2
     return s[start:end+1]
solution = Solution()
print(solution.longestpalindrome("babad"))
print(solution.longestpalindrome("cbbd"))




