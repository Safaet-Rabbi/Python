n = int(input())
letters = list(map(int, input().split()))
unread_indices = [i for i in range(n) if letters[i] == 1]
if len(unread_indices) == 0:
    print(0)
else:
    operations = len(unread_indices)
    for i in range(1, len(unread_indices)):
        if unread_indices[i] - unread_indices[i-1] > 1:
            operations += 1
    print(operations)
