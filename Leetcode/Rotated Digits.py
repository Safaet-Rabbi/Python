class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_same = {'0', '1', '8'}
        valid_diff = {'2', '5', '6', '9'}
        
        count = 0
        
        for num in range(1, n + 1):
            s = str(num)
            is_valid = True
            has_diff = False
            
            for ch in s:
                if ch in valid_same:
                    continue
                elif ch in valid_diff:
                    has_diff = True
                else:
                    is_valid = False
                    break
            
            if is_valid and has_diff:
                count += 1
        
        return count