def find_seats(n, bus_rows):
    for i in range(n):
        if bus_rows[i][:2] == 'OO':  # Check first pair of seats in the row
            bus_rows[i] = '++' + bus_rows[i][2:]  # Replace the pair with '++'
            print("YES")
            print("\n".join(bus_rows))
            return
        elif bus_rows[i][3:] == 'OO':  # Check second pair of seats in the row
            bus_rows[i] = bus_rows[i][:3] + '++'
            print("YES")
            print("\n".join(bus_rows))
            return
    
    print("NO")

n = int(input().strip())
bus_rows = [input().strip() for _ in range(n)]

find_seats(n, bus_rows)
