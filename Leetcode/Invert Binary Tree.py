class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if (not root) or (not root.left and not root.right):
                return
            root.left, root.right = root.right, root.left
            invert(root.left)
            invert(root.right)
        invert(root)
        return root