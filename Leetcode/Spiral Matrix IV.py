class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        top, bottom, left, right = 0, m - 1, 0, n - 1
        current = head
        while current:
            for i in range(left, right + 1):
                if current:
                    matrix[top][i] = current.val
                    current = current.next
            top += 1
            for i in range(top, bottom + 1):
                if current:
                    matrix[i][right] = current.val
                    current = current.next
            right -= 1  
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    if current:
                        matrix[bottom][i] = current.val
                        current = current.next
                bottom -= 1 
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if current:
                        matrix[i][left] = current.val
                        current = current.next
                left += 1 
        
        return matrix
