class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        i = 0
        for i in arr:
            if arr.count(i) / float(n) > 0.25:
                break
        return i