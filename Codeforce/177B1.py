def max_game_result(n):
    result = 0
    while n > 1:
        result += n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                n //= i 
                break
        else:
            n = 1
    
    result += 1
    return result
n = int(input())
print(max_game_result(n))
