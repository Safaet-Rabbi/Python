class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {1000 : "M", 900 : "CM", 500 : "D", 400 : "CD", 100 : "C", 90 : "XC", 50 :        "L", 40 : "XL", 10 : "X", 9 : "IX", 5 : "V", 4 : "IV",1 : "I"}
        result=''
        for i in num_map:
            while num>=i:
                result+=num_map[i]
                num=num-i
        return result    
solution = Solution()
print(solution.intToRoman(3749))  
print(solution.intToRoman(58))    
print(solution.intToRoman(1994)) 
