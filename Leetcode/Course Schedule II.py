from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        zero_in_degree_queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        topo_order = []
        
        while zero_in_degree_queue:
            node = zero_in_degree_queue.popleft()
            topo_order.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree_queue.append(neighbor)
        
        if len(topo_order) == numCourses:
            return topo_order
        else:
            return []
