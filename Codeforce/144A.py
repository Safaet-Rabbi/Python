def get_minimum_swaps(heights):
  swaps = 0
  if heights[0] != heights[-1]:
    swaps += 1
  for i in range(1, len(heights) - 1):
    if heights[i] > heights[i + 1]:
      swaps += 1
      heights[i], heights[i + 1] = heights[i + 1], heights[i]
      break

  return swaps


n = int(input())

heights = [int(input()) for _ in range(n)]
heights.sort(reverse=True)

swaps = get_minimum_swaps(heights.copy())

print(swaps)
