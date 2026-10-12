class Solution:
    def dayOfYear(self, date: str) -> int:
        m = int(date[5:7])
        n = (0,31,59,90,120,151,181,212,243,273,304,334)[m-1] + int(date[8:])
        if m > 2:
            y = int(date[:4])
            if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                n += 1
        return n