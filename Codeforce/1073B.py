def vasya_and_books(n, a, b):
    position = {book: i for i, book in enumerate(a)}
    max_position_removed = -1
    
    result = []
    
    for book in b:
        if position[book] > max_position_removed:
            books_to_move = position[book] - max_position_removed
            result.append(books_to_move)
            max_position_removed = position[book]
        else:
            result.append(0)
    
    return result
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = vasya_and_books(n, a, b)
print(' '.join(map(str, result)))
