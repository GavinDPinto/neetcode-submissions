# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Sketch: go inorder, add to list and then pick the [k+1] index 
        def listify(node) -> list[int]:
            if not node:
                return []
            left_list = listify(node.left)
            right_list = listify(node.right)
            left_list.append(node.val)
            left_list.extend(right_list)
            return left_list
        
        return listify(root)[k-1]