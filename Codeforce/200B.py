n = int(input()) 
percentages = list(map(int, input().split())) 
average_percentage = sum(percentages) / n
print(f"{average_percentage:.12f}")
