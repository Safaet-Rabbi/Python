def can_tile(board, n):
    def can_place_piece(i, j):
        if (board[i][j] == '.' and
                board[i - 1][j] == '.' and
                board[i + 1][j] == '.' and
                board[i][j - 1] == '.' and
                board[i][j + 1] == '.'):
            board[i][j] = '#'
            board[i - 1][j] = '#'
            board[i + 1][j] = '#'
            board[i][j - 1] = '#'
            board[i][j + 1] = '#'
            return True
        return False
    board = [list(row) for row in board]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if board[i][j] == '.':
                can_place_piece(i, j)
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                return "NO"
    
    return "YES"
n = int(input())
board = [input().strip() for _ in range(n)]
result = can_tile(board, n)
print(result)
