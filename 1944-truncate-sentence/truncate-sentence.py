class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        list1 = list(s.split(' '))
        return (" ".join(list1[:k]))
            
        