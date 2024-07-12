def polycarp_training(n, contests):
    contests.sort()
    days = 0
    for i in range(n):
        if contests[i] >= days + 1:
            days += 1
    return days
n = int(input())
contests = list(map(int, input().split()))
print(polycarp_training(n, contests))
