from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            elements = []

            top, left = layer, layer
            bottom, right = m - layer - 1, n - layer - 1

            # Top row
            for j in range(left, right + 1):
                elements.append(grid[top][j])

            # Right column
            for i in range(top + 1, bottom):
                elements.append(grid[i][right])

            # Bottom row
            for j in range(right, left - 1, -1):
                elements.append(grid[bottom][j])

            # Left column
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])

            # Rotate counter-clockwise
            length = len(elements)
            rot = k % length
            rotated = elements[rot:] + elements[:rot]

            idx = 0

            # Put back Top row
            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1

            # Put back Right column
            for i in range(top + 1, bottom):
                grid[i][right] = rotated[idx]
                idx += 1

            # Put back Bottom row
            for j in range(right, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1

            # Put back Left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1

        return grid