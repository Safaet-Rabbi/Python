def min_flips_to_verify_statement(s):
    vowels = set('aeiou')
    odd_digits = set('13579')
    
    flips_needed = 0
    
    for char in s:
        if char in vowels or char in odd_digits:
            flips_needed += 1
    
    return flips_needed

if __name__ == "__main__":    
    s = input().strip()
    result = min_flips_to_verify_statement(s)
    print(result)
