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
        lcur = head
        rcur = slow.next

        # reverse [m+1 ... n-1]
        prev = None
        while rcur:
            next = rcur.next
            rcur.next = prev
            prev = rcur
            rcur = next
        rcur = prev

        # 0 -> n-1 -> 1 -> n-2 -> 2 -> ... till either null, then return ret
        cur = head
        lcur = lcur.next
        while lcur != slow.next or rcur:
            if cur:
                cur.next = rcur
                cur = cur.next
            if rcur:
                rcur = rcur.next
            if cur:
                cur.next = lcur
                cur = cur.next
            if lcur:
                lcur = lcur.next
        if cur:
            cur.next = None