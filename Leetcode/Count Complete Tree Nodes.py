class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left =  dfs(node.left)
            right = dfs(node.right)

            return 1 + left + right

        return dfs(root)

            
        