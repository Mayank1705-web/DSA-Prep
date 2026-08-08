class Solution(object):
    def getHours(self, piles, mid):
        ans = 0
        for pile in piles:
            ans += (pile + mid - 1) // mid
        return ans
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = k = max(piles)

        while l <= r:
            mid = (l+r) // 2
            if self.getHours(piles,mid) > h:
                l = mid + 1
            else:
                k = mid
                r = mid - 1
        return k