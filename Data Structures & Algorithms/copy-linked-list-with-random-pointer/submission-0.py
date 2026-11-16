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
        node_map = {}
        cur = head
        while cur:
            copy = Node(cur.val)
            node_map[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = node_map[cur]
            copy.next = node_map[cur.next] if cur.next else None
            copy.random = node_map[cur.random] if cur.random else None
            cur = cur.next
        return node_map[head] if head else None