def max_reward(n):
    reward = 0.0
    for i in range(1, n + 1):
        reward += 1 / i
    return reward
n = int(input().strip())
result = max_reward(n)
print(f"{result:.12f}")
