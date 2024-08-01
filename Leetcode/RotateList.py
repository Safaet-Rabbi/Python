class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if head == None:
            return head
        l = 1
        temp = head
        while temp.next:
            temp = temp.next
            l += 1

        k = k % l
        n = l - k

        temp.next = head
        while n != 0:
            temp = temp.next
            n -= 1

        head = temp.next
        temp.next = None
        return head

        