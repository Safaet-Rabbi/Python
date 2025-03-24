class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_occurrence = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            for larger_digit in range(9, int(d), -1):
                if last_occurrence.get(larger_digit, -1) > i:
                    digits[i], digits[last_occurrence[larger_digit]] = digits[last_occurrence[larger_digit]], digits[i]
                    return int(''.join(digits))
        
        return num
