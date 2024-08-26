n = int(input())
ticket = input()
first_half = sorted(ticket[:n])
second_half = sorted(ticket[n:])
all_less = all(first_half[i] < second_half[i] for i in range(n))
all_greater = all(first_half[i] > second_half[i] for i in range(n))
if all_less or all_greater:
    print("YES")
else:
    print("NO")
