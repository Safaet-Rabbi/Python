class Solution:
    def lengthOfLongestSubstring(self,s):
        index_map = {}
        start = 0
        max_length = 0
        for end in range(len(s)):
            if s[end] in index_map:
                start = max(start, index_map[s[end]]+1)
            index_map[s[end]] = end
            max_length = max(max_length,end - start + 1)
        return max_length
