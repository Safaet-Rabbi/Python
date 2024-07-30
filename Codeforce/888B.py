def max_correct_commands(n, commands):
    up_count = commands.count('U')
    down_count = commands.count('D')
    left_count = commands.count('L')
    right_count = commands.count('R')
    vertical_pairs = min(up_count, down_count)
    horizontal_pairs = min(left_count, right_count)
    
    return 2 * (vertical_pairs + horizontal_pairs)

n = int(input().strip())
commands = input().strip()
print(max_correct_commands(n, commands))
