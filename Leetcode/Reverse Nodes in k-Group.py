class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse_linked_list(head, k):
            prev, curr = None, head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev
        
        count = 0
        ptr = head      
        while count < k and ptr:
            ptr = ptr.next
            count += 1       
        if count == k:
            reversed_head = reverse_linked_list(head, k)           
            head.next = self.reverseKGroup(ptr, k)            
            return reversed_head     
        return head
