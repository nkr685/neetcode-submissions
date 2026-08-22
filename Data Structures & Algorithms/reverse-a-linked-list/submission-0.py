# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        prev = None
        next = None
        while True:
            tmp = prev
            next = head.next
            head.next = tmp
            prev = head
            if not next:
                break
            head = next
        return head