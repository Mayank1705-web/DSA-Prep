class Solution:
    def sumOfMultiples(self, n):
        r = self.gauss(n, 3) + self.gauss(n, 5) + self.gauss(n, 7)
        r -= self.gauss(n, 15) + self.gauss(n, 21) + self.gauss(n, 35)
        r += self.gauss(n, 105)
        return r

    def gauss(self, n, step):
        if step == 1:
            return (n * (n + 1)) // 2
        return step * self.gauss(n // step, 1)