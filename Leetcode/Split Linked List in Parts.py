class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        part_size = length // k
        extra_parts = length % k  

        parts = []
        current = head
        for i in range(k):
            part_head = current
            current_part_size = part_size + (1 if extra_parts > 0 else 0)
            extra_parts -= 1

            for j in range(current_part_size - 1):
                if current:
                    current = current.next

            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            parts.append(part_head)

        return parts
