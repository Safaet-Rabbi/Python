def make_product_equal_one(n, numbers):
    cost = 0
    count_negative = 0
    count_zero = 0
    for num in numbers:
        if num > 1:
            cost += (num - 1)
        elif num < -1:
            cost += (-1 - num)
            count_negative += 1
        elif num == 0:
            cost += 1
            count_zero += 1
        elif num == -1:
            count_negative += 1
    if count_negative % 2 != 0:
        if count_zero > 0:
            cost += 0  
        else:
            cost += 2  

    return cost
n = int(input())
numbers = list(map(int, input().split()))
result = make_product_equal_one(n, numbers)
print(result)
