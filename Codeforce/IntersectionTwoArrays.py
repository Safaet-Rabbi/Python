from collections import Counter
class Solution:
    def intersect(self, nums1, nums2) :
        count1 = Counter(nums1)
        result = []
        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1  

        return result
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
sol = Solution()
print(sol.intersect(nums1, nums2)) 
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(sol.intersect(nums1, nums2)) 
