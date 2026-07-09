class Solution(object):
    def decimalRepresentation(self, n):
        #dsa
        res = []
        power = 0
        while n > 0:
            r = n % 10
            if r != 0:
                res.append(r * 10 ** power)
            n //= 10
            power +=1
        return res[::-1]
            
        