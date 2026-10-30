# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def maxDepth(node):
            nonlocal max_diameter
            if not node:
                return 0
            right_max = maxDepth(node.right)
            left_max = maxDepth(node.left)
            if right_max + left_max > max_diameter:
                max_diameter = right_max + left_max
            return 1 + max(right_max, left_max)
        
        maxDepth(root)

        return max_diameter