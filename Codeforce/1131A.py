def calculate_marked_cells(w1, h1, w2, h2):
    marked_cells = 2 * (h1 + h2) + 2 * w1 + 4
    return marked_cells

w1, h1, w2, h2 = map(int, input().strip().split())
result = calculate_marked_cells(w1, h1, w2, h2)
print(result)
