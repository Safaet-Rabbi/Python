def minimum_redo(n, grades):
    total = sum(grades)
    current_average = total / n
    if current_average >= 4.5:
        return 0
    grades.sort()
    count = 0
    while current_average < 4.5:
        total += (5 - grades[count])
        count += 1
        current_average = total / n
    
    return count
n = int(input().strip())
grades = list(map(int, input().strip().split()))
min_redo = minimum_redo(n, grades)
print(min_redo)
