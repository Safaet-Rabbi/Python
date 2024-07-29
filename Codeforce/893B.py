def find_greatest_beautiful_divisor(n):
    beautiful_numbers = []
    k = 1
    while True:
        beautiful_number = (2 ** (k + 1) - 1) * (2 ** k)
        if beautiful_number > n:
            break
        beautiful_numbers.append(beautiful_number)
        k += 1  
    beautiful_numbers.reverse()
    
    for beautiful_number in beautiful_numbers:
        if n % beautiful_number == 0:
            return beautiful_number
    
    return 1
n = int(input())
result = find_greatest_beautiful_divisor(n)
print(result)
