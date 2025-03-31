class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))
        events.sort()

        max_groups = curr_groups = 0
        for _, count in events:
            curr_groups += count
            max_groups = max(max_groups, curr_groups)

        return max_groups
