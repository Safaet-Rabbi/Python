def find_kth_identifier(n, k, identifiers):
    cumulative_count = [0] * n
    cumulative_count[0] = 1
    for i in range(1, n):
        cumulative_count[i] = cumulative_count[i - 1] + (i + 1)

    robot_index = 0
    while robot_index < n and cumulative_count[robot_index] < k:
        robot_index += 1
    
    if robot_index == 0:
        return identifiers[0]
    
    previous_total = cumulative_count[robot_index - 1]
    position_within_robot = k - previous_total - 1
    return identifiers[position_within_robot]
if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    identifiers = list(map(int, input().strip().split()))
    result = find_kth_identifier(n, k, identifiers)
    print(result)
