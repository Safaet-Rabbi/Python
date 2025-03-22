class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findKthBitHelper(n, k):
            if n == 1:
                return '0'
            length = (1 << n) - 1 
            mid = length // 2 + 1
            if k == mid:
                return '1'
            elif k < mid:
                return findKthBitHelper(n - 1, k)
            else:
                return '1' if findKthBitHelper(n - 1, length - k + 1) == '0' else '0'
        
        return findKthBitHelper(n, k)
