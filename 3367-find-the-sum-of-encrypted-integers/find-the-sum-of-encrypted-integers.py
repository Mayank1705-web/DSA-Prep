class Solution(object):
    def sumOfEncryptedInt(self, nums):
        a=0
        for x in nums:
            b=max(int(y) for y in str(x))
            a+=int(str(b)*len(str(x)))
        return a