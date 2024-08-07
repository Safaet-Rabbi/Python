class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }      
        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return
            possible_letters = digit_to_letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  #Remove the last character to backtrack
        
        combinations = []
        backtrack(0, [])
        return combinations
