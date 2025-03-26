class Solution:
    def minimumSteps(self, s: str) -> int:
        ones_count = 0
        result = 0
        for i, c in enumerate(s):
            if c == '1':
                ones_count += 1
            else:
                result += ones_count
        return result
