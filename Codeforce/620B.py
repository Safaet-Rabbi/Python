def calculate_segments(a, b):
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    total_segments = 0
    
    for number in range(a, b + 1):
        while number > 0:
            digit = number % 10
            total_segments += segments[digit]
            number //= 10
    
    return total_segments

a, b = map(int, input().split())
print(calculate_segments(a, b))
