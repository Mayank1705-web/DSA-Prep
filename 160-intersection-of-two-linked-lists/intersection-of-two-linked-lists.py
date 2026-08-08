# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1 = len2 = 0
        curr1, curr2 = headA, headB
        while curr1 != None:
            len1 += 1
            curr1 = curr1.next
        while curr2 != None:
            len2 += 1
            curr2 = curr2.next

        diff = 0
        if len1 > len2:
            diff = len1 - len2
            for i in range(diff):
                headA = headA.next
        else:
            diff = len2 - len1
            for i in range(diff):
                headB = headB.next
        while True:
            if headA == headB:
                return headA
            else:
                headA = headA.next 
                headB = headB.next
        return None