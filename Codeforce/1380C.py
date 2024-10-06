def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        teams = 0
        count = 0
        for skill in a:
            count += 1
            if count * skill >= x:
                teams += 1
                count = 0
        print(teams)

solve()
