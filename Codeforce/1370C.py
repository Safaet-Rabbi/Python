t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print("FastestFinger")
    elif n == 2 or n % 2 == 1:
        print("Ashishgup")
    elif (n & (n - 1)) == 0:
        print("FastestFinger")
    elif n % 4 != 0 and all(n % i != 0 for i in range(3, int(n ** 0.5) + 1, 2)):
        print("FastestFinger")
    else:
        print("Ashishgup")
