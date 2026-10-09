# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        behind, ahead = head, head
        for i in range(n + 1):
            if ahead:
                ahead = ahead.next
            else:
                return head.next # n = size of list
        
        while ahead:
            behind, ahead = behind.next, ahead.next
        
        behind.next = behind.next.next

        return head
        
        
        