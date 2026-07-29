class Solution(object):
    def isPalindrome(self, x):
        if x < 0: 
            return False
        a = 0
        copy = x

        while (x > 0):
            a = a * 10 + (x % 10)
            x //= 10
        
        return a == copy


        