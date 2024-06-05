def find_nth_digit(n):
    digit_length = 1
    count = 9
    start = 1

    while n > digit_length * count:
        n -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10

    number = start + (n - 1) // digit_length
    digit_index = (n - 1) % digit_length
    return str(number)[digit_index]

n = int(input().strip())

print(find_nth_digit(n))
