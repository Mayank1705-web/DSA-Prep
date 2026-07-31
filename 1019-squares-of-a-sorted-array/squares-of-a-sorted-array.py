class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(list(map(lambda x: x ** 2, nums)))
        