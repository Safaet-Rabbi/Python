class Solution:
    def convert(self,s,numRows):
        if(numRows < 2):
            return s
        arr = ['' for i in range(numRows)]
        direction = 'down'
        row = 0
        for i in s:
            arr[row] += i
            if row == numRows-1:
                direction = 'up'
            elif row == 0:
                direction = 'down'
            if(direction == 'down'):
                row += 1
            else:
                row -= 1
        return(''.join(arr))
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  
print(solution.convert("PAYPALISHIRING", 4)) 
print(solution.convert("A", 1))