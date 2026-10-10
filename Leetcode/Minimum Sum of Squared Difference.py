class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff_counter = Counter(abs(num1 - num2) for num1, num2 in zip(nums1, nums2))
        diff_counter[0] = 0
        sorted_diffs = sorted(diff_counter)
        max_diff = sorted_diffs.pop()

        while sorted_diffs and k:
            next_diff = sorted_diffs.pop()
            max_diff_freq = diff_counter.pop(max_diff)
            height = max_diff - next_diff
            area = height * max_diff_freq

            if k >= area:
                k -= area
                diff_counter[next_diff] += max_diff_freq
            else:
                full_rows, short_count = divmod(k, max_diff_freq)
                tall_count = max_diff_freq - short_count
                tall = max_diff - full_rows
                short = tall - 1
                diff_counter[tall] += tall_count
                diff_counter[short] += short_count
                break

            max_diff = next_diff
        return sum(diff * diff * freq for diff, freq in diff_counter.items() if diff)