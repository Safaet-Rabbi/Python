class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        def split(head):
            slow, fast = head, head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return head, slow
        
        def merge(left, right):
            dummy = ListNode(0)
            current = dummy
            while left and right:
                if left.val <= right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next
            if left:
                current.next = left
            if right:
                current.next = right
            return dummy.next
        
        left, right = split(head)
        left = self.sortList(left)
        right = self.sortList(right)
        return merge(left, right)
