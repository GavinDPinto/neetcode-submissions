# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, largest = float('-inf')) -> int:
        if not root:
            return 0
        lgn = self.goodNodes(root.left, max(largest, root.val))
        rgn = self.goodNodes(root.right, max(largest, root.val))
        if root.val >= largest:
            return 1 + lgn + rgn
        return lgn + rgn
        