class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, list1, list2):
        l1 = list1
        l2 = list2
        carry = 0
        result = ListNode(0)
        temp = result
        
        while l1 is not None or l2 is not None:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next
            temp.next = ListNode(carry % 10)
            temp = temp.next
            carry = carry // 10
        
        if carry == 1:
            temp.next = ListNode(carry)
        
        return result.next

# Helper functions to create linked lists and print them
def create_linked_list(elements):
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output: 7 -> 0 -> 8 -> None
l3 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l4 = create_linked_list([9, 9, 9, 9])
result2 = solution.addTwoNumbers(l3, l4)
print_linked_list(result2)  # Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 -> None
