class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacle_set = set(map(tuple, obstacles))       
        x, y = 0, 0
        direction_index = 0  
        
        max_distance_sq = 0
        
        for command in commands:
            if command == -1:  
                direction_index = (direction_index + 1) % 4
            elif command == -2:  
                direction_index = (direction_index - 1 + 4) % 4
            else:
                dx, dy = directions[direction_index]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_distance_sq = max(max_distance_sq, x * x + y * y)
                    else:
                        break
        
        return max_distance_sq
