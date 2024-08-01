class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        ptr = head
        while ptr:
            newNode = Node(ptr.val)
            newNode.next = ptr.next
            ptr.next = newNode
            ptr = newNode.next

        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        ptrOld = head
        ptrNew = head.next
        headNew = ptrNew
        while ptrOld:
            ptrOld.next = ptrNew.next
            ptrNew.next = ptrNew.next.next if ptrNew.next else None

            ptrOld = ptrOld.next
            ptrNew = ptrNew.next

        return headNew