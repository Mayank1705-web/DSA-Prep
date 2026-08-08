class Solution(object):
    def sortArrayByParity(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        j = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        return arr