def can_be_corrected(n, sequence):
    if n % 2 != 0:
        return "No"

    balance = 0
    for char in sequence:
        if char == '(':
            balance += 1
        else:
            balance -= 1

        if balance < -1:
            return "No"

    return "Yes" if abs(balance) <= 1 else "No"

n = int(input())
sequence = input()
print(can_be_corrected(n, sequence))
