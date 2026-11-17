# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry over method (elementary school method)
        head = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        cur = head
        cur1 = l1.next
        cur2 = l2.next
        while (cur1 or cur2):
            if not cur1:
                newnode = ListNode((cur2.val + carry) % 10)
                carry = (cur2.val + carry) // 10
                cur.next = newnode
                cur = newnode
                cur2 = cur2.next
            elif not cur2:
                newnode = ListNode((cur1.val + carry) % 10)
                carry = (cur1.val + carry) // 10
                cur.next = newnode
                cur = newnode
                cur1 = cur1.next
            else:
                newnode = ListNode((cur1.val + cur2.val + carry) % 10)
                carry = (cur1.val + cur2.val + carry) // 10
                cur.next = newnode
                cur = newnode
                cur1 = cur1.next
                cur2 = cur2.next
        if carry:
            newnode = ListNode(carry)
            cur.next = newnode
        return head
