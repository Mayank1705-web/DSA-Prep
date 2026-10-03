class Solution(object):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        return abs(self.daysFrom1971(date1) - self.daysFrom1971(date2))

    def isLeap(self, y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    def daysFrom1971(self, dt):
        y = int(dt[0:4])
        m = int(dt[5:7])
        d = int(dt[8:10])

        for iy in range(1971, y):
            d += 366 if self.isLeap(iy) else 365

        d += sum(self.days[:m - 1])

        if m > 2 and self.isLeap(y):
            d += 1

        return d
