# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        value = 0
        curr = head
        while curr:
            value += curr.val * (2 ** (length - 1))
            length -= 1
            curr = curr.next
        return value
        

        