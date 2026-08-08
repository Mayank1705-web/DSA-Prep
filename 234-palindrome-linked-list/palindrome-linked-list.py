# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        curr = head
        list_head = []
        while curr != None:
            list_head.append(curr.val)
            curr = curr.next
        if list_head == list_head[::-1]:
            return True
        return False