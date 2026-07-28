from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)
        left_half = []
        mid = ""
        
        # Iterate in alphabetical order to guarantee lexicographically smallest result
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char in counts:
                # If the frequency is odd, this character will sit in the exact middle
                if counts[char] % 2 != 0:
                    mid = char
                # Append half of the occurrences to the left side
                left_half.append(char * (counts[char] // 2))
                
        left_str = "".join(left_half)
        # The right half is simply the left half reversed
        return left_str + mid + left_str[::-1]