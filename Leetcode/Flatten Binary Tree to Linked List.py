class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        right_subtree = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = right_subtree
