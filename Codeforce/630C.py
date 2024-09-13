def count_lucky_numbers(n):
    return 2 * (2**n - 1)
n = int(input())
print(count_lucky_numbers(n))
