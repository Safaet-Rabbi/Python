class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  
        if not s:
            return 0
        sign = 1
        index = 0     
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            index += 1    
        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1      
        result *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX    
        return result
sol = Solution()
print(sol.myAtoi("   -042"))  
print(sol.myAtoi("1337c0d3"))  
print(sol.myAtoi("0-1"))      
print(sol.myAtoi("words and 987")) 
