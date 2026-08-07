class Solution:
    def minimumSum(self, num):
        a,b,c,d=sorted(str(num))
        return int(a+c) + int(b+d)