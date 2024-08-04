class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_result = 0
        operator = 1

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                current_result += operator * current_number
                operator = 1
                current_number = 0
            elif char == '-':
                current_result += operator * current_number
                operator = -1
                current_number = 0
            elif char == '(':
                stack.append(current_result)
                stack.append(operator)
                current_result = 0
                operator = 1
            elif char == ')':
                current_result += operator * current_number
                current_result *= stack.pop() 
                current_result += stack.pop() 
                current_number = 0
        current_result += operator * current_number
        return current_result

