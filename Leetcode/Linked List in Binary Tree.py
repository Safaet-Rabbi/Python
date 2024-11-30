class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def dfs(tree_node, list_node):
            if not list_node:  
                return True
            if not tree_node:  
                return False
            if tree_node.val != list_node.val:  
                return False
            
            return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)
        
        def traverse_tree(tree_node):
            if not tree_node:
                return False
            if dfs(tree_node, head):
                return True
            return traverse_tree(tree_node.left) or traverse_tree(tree_node.right)        
        return traverse_tree(root)
