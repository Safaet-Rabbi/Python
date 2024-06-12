def unhandled_crimes_count(n,events):
    available_officers = 0
    unhandled_crimes = 0
    for event in events:
        if event == -1:
            if available_officers>0:
                available_officers -= 1
            else:
                unhandled_crimes+=1
        else:
            available_officers+=event
    return unhandled_crimes

n = int(input())
events = list(map(int,input().split()))
result = unhandled_crimes_count(n,events)
print(result)