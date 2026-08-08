# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        q = head
        if not head or not head.next:
            return head
        r = head.next
        while q and r:
            q.next = r.next
            r.next = q
            p.next = r
            if q.next:
                r = q.next.next
            else:
                break
            p = q
            q = q.next
        return dummy.next
        