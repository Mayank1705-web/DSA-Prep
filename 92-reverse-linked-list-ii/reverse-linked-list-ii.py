class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):      # walk to the node just before `left`
            prev = prev.next

        curr = prev.next               # this will end up as the tail of the reversed part
        for _ in range(right - left):  # move `right - left` nodes to the front, one at a time
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next