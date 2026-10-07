# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        cur1 = list1
        cur2 = list2
        if list1.val < list2.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next
        curmain = head
        
        while (cur1 or cur2):
            if not cur1:
                curmain.next = cur2
                return head
            if not cur2:
                curmain.next = cur1
                return head
            if cur1.val < cur2.val:
                curmain.next = cur1
                curmain = cur1
                cur1 = cur1.next
            else:
                curmain.next = cur2
                curmain = cur2
                cur2 = cur2.next
        
        return head