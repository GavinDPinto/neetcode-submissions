# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], inProcess = 0) -> bool:
        if (not subRoot) and (not root):
            return True
        if (not root) or (not subRoot):
            return False
        if root.val == subRoot.val and self.isSubtree(root.left, subRoot.left, 1) and self.isSubtree(root.right, subRoot.right, 1):
            return True
        if inProcess == 1:
            return False
        return self.isSubtree(root.left, subRoot, 0) or self.isSubtree(root.right, subRoot, 0)