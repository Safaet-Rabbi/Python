def calculate_calories(a1,a2,a3,a4,s):
    calories = [a1,a2,a3,a4]
    total_calories = 0
    for char in s:
        strip_index = int(char) - 1
        total_calories+= calories[strip_index]

    return total_calories
a1,a2,a3,a4 = map(int,input().split())
s = input().strip()

result = calculate_calories(a1,a2,a3,a4,s)
print(result)