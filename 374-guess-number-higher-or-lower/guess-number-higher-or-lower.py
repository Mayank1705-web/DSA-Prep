# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            num = (low + high) // 2
            result = guess(num)
            if result == 0:
                return num
            elif result == -1:
                high = num - 1
            else:
                low = num + 1