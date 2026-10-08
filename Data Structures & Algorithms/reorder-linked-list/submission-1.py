# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find median via slow/fast, call it m
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse [m+1 ... n-1]
        prev = None
        rcur = slow.next
        slow.next = None
        while rcur:
            next = rcur.next
            rcur.next = prev
            prev = rcur
            rcur = next

        # 0 -> n-1 -> 1 -> n-2 -> 2 -> ... till either null, then return ret
        rcur = prev
        lcur = head

        while rcur:
            lnxt, rnxt = lcur.next, rcur.next
            lcur.next = rcur
            rcur.next = lnxt
            lcur = lnxt
            rcur = rnxt
        

        