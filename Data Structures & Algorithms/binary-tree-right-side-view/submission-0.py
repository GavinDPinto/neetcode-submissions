# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if root:
            q = deque([root])
            while q:
                ret.append(q[-1].val)
                for i in range(len(q)):
                    curnode = q.popleft()
                    if curnode.left:
                        q.append(curnode.left)
                    if curnode.right:
                        q.append(curnode.right)
        return ret
                    