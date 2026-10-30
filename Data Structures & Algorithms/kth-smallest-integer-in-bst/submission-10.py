# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Sketch: keep adding left children to stack; top of stack has smallest so pop and check if k is 1; if not, take right child and keep adding its left children. otherwise pop next off stack and check if k = 1; repeat until k = 1
        stack = []
        curnode = root

        while curnode or stack:
            while curnode:
                stack.append(curnode)
                curnode = curnode.left
            curnode = stack.pop()
            if k == 1:
                return curnode.val
            k -= 1
            curnode = curnode.right
        
        return -1