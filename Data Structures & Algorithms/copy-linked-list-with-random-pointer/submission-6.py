"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # pass 1: interleave copy nodes after original
        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = cur.next.next
        
        # pass 2: assign random pointers
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        
        # cut out original nodes
        head_copy = head.next
        cur = head_copy
        while cur:
            cur.next = cur.next.next if cur.next else None
            cur = cur.next
        
        return head_copy