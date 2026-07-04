class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        q = deque([1])
        visited = set([1])
        ans = float('inf')

        while q:
            node = q.popleft()
            for nei, d in graph[node]:
                ans = min(ans, d)
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return ans