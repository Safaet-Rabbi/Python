def nth_even_length_palindrome(n):
    n = int(n)
    k = str(n)
    palindrome = k + k[::-1]  
    
    return palindrome
n = input().strip()
print(nth_even_length_palindrome(n))
