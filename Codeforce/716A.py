def remaining_words(n, c, times):
    # Initially, the screen is empty
    remaining = 0
    last_time = 0
    
    for i in range(n):
        if i == 0:
            # First word typed
            remaining = 1
        else:
            # Calculate the time difference between current and last typed word
            if times[i] - last_time > c:
                # If the difference is greater than c, reset the count
                remaining = 1
            else:
                # Otherwise, just increment the count
                remaining += 1
        
        # Update the last time
        last_time = times[i]
    
    return remaining

# Take inputs from the user
n, c = map(int, input().split())
times = list(map(int, input().split()))

print(remaining_words(n, c,times))
