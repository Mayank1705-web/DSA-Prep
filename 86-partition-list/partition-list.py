# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        p = dummy = ListNode(0)
        curr = head
        while curr != None:
            if curr.val < x:
                newNode = ListNode(curr.val)
                p.next = newNode
                p = p.next
            curr = curr.next
        curr = head
        while curr != None:
            if curr.val >= x:
                newNode = ListNode(curr.val)
                p.next = newNode
                p = p.next
            curr = curr.next
    
        return dummy.next


        