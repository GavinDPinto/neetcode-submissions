# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if root:
            q = deque([root])
            while q:
                sublist = []
                for i in range(len(q)):
                    curnode = q.popleft()
                    sublist.append(curnode.val)
                    if curnode.left:
                        q.append(curnode.left)
                    if curnode.right:
                        q.append(curnode.right)
                ret.append(sublist)
        return ret
            