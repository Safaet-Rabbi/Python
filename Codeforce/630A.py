try:
    n = int(input().strip())
    
    if 2 <= n <= 2 * 10**18:
        print("25")
    else:
        raise ValueError("n is out of the valid range")
except ValueError as ve:
    print("Invalid input:", ve)
