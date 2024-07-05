class Solution:
    def reverse(self, x: int) -> int:
        if not -2**31<=x<=2**31-1:
            return int(0)
        else:
            rev=0
            negative= x < 0
            n=abs(x)
            while n!=0:
                last_d= n % 10
                rev = rev*10 + last_d
                n = n//10
            if negative:
                rev=-rev
            if  not -2**31<=rev<=2**31-1:
                return int(0)
            else:
                return rev
sol = Solution()
print(sol.reverse(123))   
print(sol.reverse(-123)) 
print(sol.reverse(120))  
